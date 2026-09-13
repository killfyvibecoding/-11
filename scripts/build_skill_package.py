#!/usr/bin/env python3
"""Build a deterministic Codex .skill archive from this repository."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]


def package_files() -> list[Path]:
    paths = [
        ROOT / "SKILL.md",
        ROOT / "LICENSE",
        ROOT / "NOTICE.md",
        ROOT / "skill-manifest.json",
        ROOT / "agents/openai.yaml",
    ]
    paths.extend(sorted((ROOT / "references").glob("*.md")))
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Output .skill path")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "skill-manifest.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    output = args.output or (ROOT / "dist" / f"ecommerce-product-visual-suite-{version}.skill")
    output.parent.mkdir(parents=True, exist_ok=True)

    files = package_files()
    missing = [path for path in files if not path.is_file()]
    if missing:
        raise SystemExit("Missing package files: " + ", ".join(str(path) for path in missing))

    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            info = ZipInfo(relative, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())

    print(f"Built {output}")
    print(f"Included {len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
