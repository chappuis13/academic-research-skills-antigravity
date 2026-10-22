# ARS → Antigravity Parity Matrix

Sumber kanonik: `Imbad0202/academic-research-skills`.

## Skill-level parity

| Skill ARS | Lokasi Antigravity | Status |
|---|---|---|
| deep-research | `.agents/skills/deep-research/SKILL.md` | Ported (kanonik di-vendor) |
| academic-paper | `.agents/skills/academic-paper/SKILL.md` | Ported (kanonik di-vendor) |
| academic-paper-reviewer | `.agents/skills/academic-paper-reviewer/SKILL.md` | Ported (kanonik di-vendor) |
| academic-pipeline | `.agents/skills/academic-pipeline/SKILL.md` | Ported (kanonik di-vendor) |
| sr-screener | `.agents/skills/sr-screener/SKILL.md` | Ported (kanonik di-vendor) |

## Mode-level parity ringkas

| Skill | Mode ARS | Implementasi Antigravity |
|---|---|---|
| deep-research | full, quick, review, lit-review, fact-check, three-way-scan, socratic, systematic-review | Sama; gunakan skill kanonik di `.agents/skills/deep-research` |
| academic-paper | full, plan, outline-only, revision, revision-coach, abstract-only, lit-review, format-convert, citation-check, disclosure, rebuttal-audit | Sama; gunakan skill kanonik di `.agents/skills/academic-paper` |
| academic-paper-reviewer | full, quick, methodology-focus, guided, re-review, calibration | Sama; gunakan skill kanonik di `.agents/skills/academic-paper-reviewer` |
| academic-pipeline | orchestrator penuh 10 stage + Stage 2.5/4.5 gates + Stage 3' re-review lane | Sama; gunakan skill kanonik di `.agents/skills/academic-pipeline` |
| sr-screener | protocol, quick, pilot, ta-screen, ft-screen, adjudicate, audit, report | Sama; gunakan skill kanonik di `.agents/skills/sr-screener` |

## Integrity gates & checkpoints

- Gate integritas Stage 2.5 dan 4.5 dipertahankan sesuai skill kanonik.
- Checkpoint manusia (MANDATORY/SLIM) dipertahankan sesuai skill kanonik.
- Handoff artifact tetap memakai referensi schema `shared/` yang di-vendor.

## Keterbatasan runtime Antigravity

1. Bila runtime tidak menyediakan subagent/hook setara Claude, orkestrasi multi-agent dijalankan berurutan (sequential fallback).
2. Independensi reviewer A/B dapat menurun bila semua langkah dijalankan dalam satu konteks runtime.
3. Hook fail-closed yang runtime-spesifik diganti validasi deterministik via skrip Python sebelum transisi stage.
4. Slash command kustom dapat tidak tersedia di runtime tertentu; gunakan fallback prompt pada `commands/antigravity-command-map.json`.
