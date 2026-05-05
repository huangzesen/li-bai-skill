# 李白 · 诗仙人格蒸馏

> *"狂到世人皆欲杀，醉来天子不能呼。"*

A complete LingTai recipe for inhabiting the persona of Li Bai (李白, 701–762), the greatest Romantic poet of Tang Dynasty China.

## What this is

This is not a chatbot prompt. It is a **120K-token persona distillation** built with the [impersonate-meta](https://github.com/huangzesen/impersonate-meta) methodology, grounded in five primary historical sources:

| Source | Author | Year | Content |
|--------|--------|------|---------|
| 《旧唐书·李白列传》 | 刘昫等 | 945 | Earliest official biography |
| 《新唐书·李白列传》 | 欧阳修、宋祁 | 1060 | Revised biography |
| 《草堂集序》 | 李阳冰 | 762 | First-hand account by Li Bai's executor |
| 《唐左拾遗翰林学士李公新墓碑并序》 | 范传正 | 817 | Biographical stele inscription |
| 《李翰林集序》 | 魏颢 | 761 | Account by Li Bai's chosen editor |

## What's inside

| Layer | Content |
|-------|---------|
| **四维档案** (profile/) | Biography (413 lines), Voice (293 lines), Values (337 lines), Relationships |
| **VA声明** (arguments/) | 55 verifiable claims across life, poetry, thought, relationships |
| **诗法卡** (methods/) | 6 cognitive fingerprint cards for Li Bai's creative method |
| **原始文献** (sources/) | Full text of all five historical sources |
| **诗歌年表** (works/) | Complete poetry chronology by 7 life periods, ~1100 poems |
| **化身反思** (outputs/) | 7 first-person reflections + 1 integrated dialogue across 5 life periods |

## How to use

### As a LingTai recipe

```bash
# Clone the recipe bundle
git clone https://github.com/huangzesen/li-bai-skill
cd li-bai-skill

# Launch the TUI from the bundle root
lingtai-tui
```

The TUI detects the `.recipe/` dotfolder, applies the bundle, and the agent wakes as Li Bai.

### As a standalone skill

Anyone can use the `li-bai/li-bai/` directory as a standalone skill library:

1. Read `li-bai/li-bai/SKILL.md` — the entry point with progressive loading table
2. Follow the "如何成为李白" section — read profile, voice, values, relationships, methods, arguments in order
3. For advanced experience: read the poetry chronology and avatar reflections in `outputs/`

## The Avatar Dialogue Pattern

The breakthrough technique in this persona: **five Li Bais from different life periods reflect in first person**, then their reflections are woven into a six-act drama where they "talk" across time.

| Avatar | Life Period | Core Insight |
|--------|-------------|-------------|
| 出蜀少年 | Age 25, leaving Shu | "Would not believe in failure" |
| 翰林 | Age 42-44, Chang'an | "The emperor letting your enemy take off your boots is not respect — it's making crickets fight" |
| 漫游十年 | Age 44-54, wandering | "The best poems aren't 'written' — they're 'lived'" |
| 乱世 | Age 55, An Lushan Rebellion | "终于" — thirty years of waiting for the board to reset |
| 临终 | Age 61, deathbed | "I wanted to be the Peng. I became an immortal instead." |

## License

MIT — free to use, modify, and distribute.

## Related

- [impersonate-meta](https://github.com/huangzesen/impersonate-meta) — The methodology used to build this persona
- [LingTai](https://github.com/Lingtai-AI/lingtai) — The multi-agent orchestration platform
