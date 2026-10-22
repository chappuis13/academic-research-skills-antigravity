# Academic Research Skills for Google Antigravity (Bahasa Indonesia)

Repository ini adalah distribusi **native Antigravity** untuk suite **Academic Research Skills (ARS)**, diparitas-kan terhadap upstream kanonik:

- Upstream: `https://github.com/Imbad0202/academic-research-skills`
- Lokasi skill Antigravity yang didukung di repo ini: **`.agents/skills/`**

## Isi utama

Lima skill ARS tersedia penuh:

1. `deep-research`
2. `academic-paper`
3. `academic-paper-reviewer`
4. `academic-pipeline`
5. `sr-screener`

Konten metodologi, mode, transisi stage, integrity gate, human checkpoint, anti-pattern, dan artifact handoff di-vendor dari sumber kanonik.

## Instalasi (project-local)

Dari root repository ini, pastikan runtime Antigravity membaca skill pada:

```text
.agents/skills/
```

## Perintah penggunaan (exact commands)

Jika runtime Anda mendukung alias slash command, gunakan alias berikut. Jika tidak, gunakan fallback prompt `[direct-mode]` yang setara.

### 1) Research

```text
/ars-research
```

Fallback:

```text
[direct-mode] deep-research full: <topik-riset>
```

### 2) Writing

```text
/ars-write
```

Fallback:

```text
[direct-mode] academic-paper full: <tujuan-penulisan>
```

### 3) Review

```text
/ars-review
```

Fallback:

```text
[direct-mode] academic-paper-reviewer full: <naskah-untuk-review>
```

### 4) Full pipeline

```text
/ars-full
```

Fallback:

```text
[direct-mode] academic-pipeline full: <proyek-penelitian>
```

### 5) Citation checking

```text
/ars-citation-check
```

Fallback:

```text
[direct-mode] academic-paper citation-check: <draft-dan-daftar-pustaka>
```

### 6) Revision

```text
/ars-revision
```

Fallback:

```text
[direct-mode] academic-paper revision: <komentar-reviewer-dan-draft>
```

### 7) Systematic-review screening

```text
/ars-screen
```

Fallback:

```text
[direct-mode] sr-screener ta-screen: <ekspor-database-dan-kriteria-inklusi-eksklusi>
```

## File penting

- `AGENTS.md` — instruksi proyek Antigravity + fallback runtime
- `docs/parity-matrix.md` — pemetaan parity skill/mode + limitation
- `commands/antigravity-command-map.json` — mapping alias command ↔ fallback prompt
- `shared/` — schema/handoff/referensi kanonik
- `scripts/` — skrip deterministik kanonik yang dipakai validasi

## Validasi lokal

```bash
python3 scripts/check_data_access_level.py .agents/skills
python3 -m unittest discover -s tests -p 'test_*.py' -v
```
