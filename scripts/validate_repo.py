#!/usr/bin/env python3
"""Validate the public repository's required files and local references."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "LICENSE",
    "NOTICE.md",
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".github/workflows/validate.yml",
    "skill-manifest.json",
    "agents/openai.yaml",
    "references/standard-asset-set.md",
    "references/detail-page-mode.md",
    "references/muyang-common-product-poster-template.md",
    "references/flowith-template-adapter.md",
    "references/flowith-template-04bb8569.md",
    "references/qa-and-recovery.md",
    "examples/generic-manifest.json",
    "scripts/build_skill_package.py",
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\n(.*?)\n---", skill_text, flags=re.S)
    if not frontmatter:
        raise SystemExit("SKILL.md is missing YAML frontmatter")
    if not re.search(r"^name:\s*ecommerce-product-visual-suite\s*$", frontmatter.group(1), flags=re.M):
        raise SystemExit("SKILL.md has an unexpected name")
    if "For this user" in skill_text or "/Users/" in skill_text:
        raise SystemExit("SKILL.md contains a local-user or absolute-path reference")

    manifest = json.loads((ROOT / "skill-manifest.json").read_text(encoding="utf-8"))
    if manifest.get("license") != "MIT":
        raise SystemExit("skill-manifest.json must declare the MIT license")
    for reference in manifest.get("references", []):
        if not (ROOT / reference).is_file():
            raise SystemExit(f"Manifest reference not found: {reference}")
    json.loads((ROOT / "examples/generic-manifest.json").read_text(encoding="utf-8"))
    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
