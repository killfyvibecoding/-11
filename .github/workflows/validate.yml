name: Validate Skill

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - name: Validate repository
        run: python scripts/validate_repo.py
      - name: Build Skill package
        run: python scripts/build_skill_package.py
