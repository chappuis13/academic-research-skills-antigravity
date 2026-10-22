import json
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".agents" / "skills"
REQUIRED_SKILLS = {
    "deep-research",
    "academic-paper",
    "academic-paper-reviewer",
    "academic-pipeline",
    "sr-screener",
}


class TestAntigravitySkillPort(unittest.TestCase):
    def test_skill_discovery(self):
        actual = {p.name for p in SKILLS_ROOT.iterdir() if p.is_dir()}
        self.assertTrue(REQUIRED_SKILLS.issubset(actual))

    def test_skill_frontmatter(self):
        for skill in sorted(REQUIRED_SKILLS):
            skill_md = SKILLS_ROOT / skill / "SKILL.md"
            self.assertTrue(skill_md.exists(), f"Missing {skill_md}")
            text = skill_md.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), f"Missing frontmatter in {skill_md}")
            m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
            self.assertIsNotNone(m, f"Unparseable frontmatter in {skill_md}")
            fm = m.group(1)
            self.assertRegex(fm, rf"(?m)^name:\s*{re.escape(skill)}\s*$")
            self.assertRegex(fm, r"(?m)^description:\s*")
            self.assertRegex(fm, r"(?m)^metadata:\s*$")

    def test_relative_markdown_links_resolve(self):
        link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        missing = []
        for skill in sorted(REQUIRED_SKILLS):
            skill_md = SKILLS_ROOT / skill / "SKILL.md"
            text = skill_md.read_text(encoding="utf-8")
            for target in link_re.findall(text):
                target = target.strip()
                if target.startswith(("http://", "https://", "#")):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                local = (skill_md.parent / target).resolve()
                root_fallback = (REPO_ROOT / target).resolve()
                if not local.exists() and not root_fallback.exists():
                    missing.append((skill, target))
        self.assertEqual([], missing, f"Missing linked paths: {missing[:10]}")

    def test_command_mapping(self):
        mapping_path = REPO_ROOT / "commands" / "antigravity-command-map.json"
        self.assertTrue(mapping_path.exists())
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        self.assertEqual(".agents/skills", mapping["installation_path"])

        commands = mapping["commands"]
        required = {
            "research",
            "writing",
            "review",
            "full_pipeline",
            "citation_check",
            "revision",
            "sr_screening",
        }
        self.assertTrue(required.issubset(commands.keys()))

        for name in required:
            entry = commands[name]
            self.assertTrue(entry["alias"].startswith("/ars-"))
            self.assertIn(entry["skill"], REQUIRED_SKILLS)
            self.assertTrue(entry["fallback_prompt"].startswith("[direct-mode]"))

    def test_deterministic_scripts(self):
        cmd = [
            "python3",
            str(REPO_ROOT / "scripts" / "check_data_access_level.py"),
            "--path",
            str(REPO_ROOT),
        ]
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, msg=result.stdout + result.stderr)

        # check_pipeline_integrity deterministic output check on identical input
        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            phase5 = td_path / "phase5_review"
            phase5.mkdir()
            (phase5 / "devils_advocate_report.md").write_text("ok", encoding="utf-8")
            (phase5 / "editor_in_chief_report.md").write_text("ok", encoding="utf-8")
            (phase5 / "ethics_review_report.md").write_text("ok", encoding="utf-8")

            cmd_json = [
                "python3",
                str(REPO_ROOT / "scripts" / "check_pipeline_integrity.py"),
                "--json",
                str(td_path),
            ]
            r1 = subprocess.run(cmd_json, check=False, capture_output=True, text=True)
            r2 = subprocess.run(cmd_json, check=False, capture_output=True, text=True)
            self.assertEqual(0, r1.returncode, msg=r1.stdout + r1.stderr)
            self.assertEqual(0, r2.returncode, msg=r2.stdout + r2.stderr)
            self.assertEqual(r1.stdout, r2.stdout)


if __name__ == "__main__":
    unittest.main()
