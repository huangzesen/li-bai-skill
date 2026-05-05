#!/usr/bin/env python3
"""
extract_page.py — Extract text content from ctext.org wiki pages.

Usage: python3 extract_page.py <url> [--simplified]

Since ctext.org blocks automated access directly, this script uses
the Wayback Machine (web.archive.org) as a proxy to retrieve cached pages.

Falls back to direct fetch with browser-like headers if archive is unavailable.
"""

import sys
import re
import html as html_mod
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def fetch_html(url: str) -> str:
    """Fetch HTML from URL, trying Wayback Machine first, then direct."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    # Try Wayback Machine first
    archive_url = f"https://web.archive.org/web/2025/{url}"
    try:
        req = Request(archive_url, headers=headers)
        resp = urlopen(req, timeout=30)
        html = resp.read().decode('utf-8')
        if 'Access unavailable' not in html and len(html) > 10000:
            print(f"[INFO] Fetched from Wayback Machine: {len(html)} bytes", file=sys.stderr)
            return html
    except (HTTPError, URLError) as e:
        print(f"[WARN] Wayback Machine failed: {e}", file=sys.stderr)

    # Try direct fetch
    try:
        req = Request(url, headers=headers)
        resp = urlopen(req, timeout=30)
        html = resp.read().decode('utf-8')
        if 'Access unavailable' not in html:
            print(f"[INFO] Fetched directly: {len(html)} bytes", file=sys.stderr)
            return html
        else:
            raise RuntimeError("Access blocked by ctext.org")
    except (HTTPError, URLError) as e:
        raise RuntimeError(f"Failed to fetch page: {e}")


def extract_text_cells(html: str, to_simplified: bool = False) -> list[dict]:
    """Extract text cells from ctext.org wiki page HTML.

    Returns list of dicts with 'index' and 'text' keys.
    Text cells are in <td class="ctext"> tags.
    """
    pattern = r'<td class="ctext"[^>]*>(.*?)</td>'
    matches = re.findall(pattern, html, re.DOTALL)

    results = []
    for i, raw in enumerate(matches):
        # Strip HTML tags
        text = re.sub(r'<[^>]+>', '', raw)
        text = html_mod.unescape(text).strip()
        if not text:
            continue

        # Skip pure page numbers
        if re.match(r'^\d+$', text):
            continue

        if to_simplified:
            try:
                import opencc
                converter = opencc.OpenCC('t2s')
                text = converter.convert(text)
            except ImportError:
                print("[WARN] opencc not installed, returning traditional Chinese",
                      file=sys.stderr)

        results.append({'index': i, 'text': text})

    return results


def extract_page_title(html: str) -> str:
    """Extract page title from ctext.org HTML."""
    m = re.search(r'<h2 class="wikisectiontitle">(.*?)<', html)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1))
        return html_mod.unescape(title).strip()

    m = re.search(r'<meta name="twitter:title" content="([^"]*)"', html)
    if m:
        return html_mod.unescape(m.group(1)).strip()
    return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_page.py <ctext_url> [--simplified]", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    to_simplified = '--simplified' in sys.argv

    html = fetch_html(url)
    title = extract_page_title(html)
    cells = extract_text_cells(html, to_simplified)

    if title:
        print(f"# {title}\n")

    for cell in cells:
        print(cell['text'])
        print()

    print(f"\n[INFO] Extracted {len(cells)} text sections", file=sys.stderr)


if __name__ == '__main__':
    main()
