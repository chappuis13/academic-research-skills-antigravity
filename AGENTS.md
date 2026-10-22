# AGENTS.md

Distribusi ini adalah port **Google Antigravity** dari repository kanonik:
`https://github.com/Imbad0202/academic-research-skills`.

## Lokasi instalasi skill yang didukung

Lokasi resmi yang didukung pada distribusi ini:

- `./.agents/skills/`

Lima skill utama tersedia di lokasi tersebut:

- `deep-research`
- `academic-paper`
- `academic-paper-reviewer`
- `academic-pipeline`
- `sr-screener`

## Aturan parity

- Konten metodologi akademik, mode, transisi stage, integrity gate, checkpoint manusia, anti-pattern, dan handoff artifact dipertahankan dari upstream.
- File kanonik juga disimpan di root repo (`deep-research/`, `academic-paper/`, dll.) agar referensi lintas-skill tetap tersedia dari clone baru.
- `shared/` dan skrip Python deterministik yang relevan ikut di-vendor untuk operasi offline dari clone baru.

## Adaptasi runtime Antigravity

Instruksi yang Claude-spesifik tidak dihapus dari skill kanonik; implementasi Antigravity memakai aturan berikut:

1. **Subagent orchestration**
   - Jika runtime Antigravity tidak menyediakan subagent paralel yang setara, jalankan langkah agent secara **berurutan** dengan urutan stage asli.
   - Deteriorasi perilaku harus diungkapkan ke pengguna (mis. reviewer A/B tidak benar-benar independen bila dijalankan serial dalam satu konteks).

2. **Hooks/guards**
   - Jika hook native tidak tersedia, jalankan guard deterministik via skrip Python yang disediakan (mis. `scripts/check_pipeline_integrity.py`, `scripts/check_data_access_level.py`) sebelum lanjut stage berikutnya.
   - Integrity gate wajib tetap dijalankan; tidak boleh dilewati diam-diam.

3. **User confirmations**
   - Semua checkpoint manusia yang bersifat mandatory/slim tetap wajib meminta konfirmasi eksplisit pengguna.

4. **Command aliases**
   - Jika runtime tidak mendukung slash command kustom, gunakan fallback prompt eksplisit di `commands/antigravity-command-map.json`.

## Validasi cepat setelah instalasi

```bash
python3 scripts/check_data_access_level.py .agents/skills
python3 -m unittest discover -s tests -p 'test_*.py' -v
```
