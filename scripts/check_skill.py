#!/usr/bin/env python3
"""Validate every skill's SKILL.md frontmatter and package each skill folder into dist/."""

import re
import sys
import zipfile
from pathlib import Path

DESCRIPTION_MAX_LENGTH = 500

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
DIST_DIR = REPO_ROOT / "dist"


def parse_frontmatter(text):
    """Return the raw frontmatter block between the leading --- markers, or None."""
    match = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    return match.group(1) if match else None


def extract_field(frontmatter, field):
    """Pull a top-level `field: value` (single or multi-line `>` block) out of frontmatter."""
    match = re.search(rf"^{field}:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if value in (">", "|", ">-", "|-", ""):
        # Multi-line block scalar: collect the indented lines that follow.
        lines = []
        rest = frontmatter[match.end():].splitlines()
        for line in rest:
            if line.strip() == "" or line.startswith((" ", "\t")):
                lines.append(line.strip())
            else:
                break
        return " ".join(lines).strip()
    return value.strip("\"'")


def check_skill(skill_md):
    skill_dir = skill_md.parent
    name = skill_dir.name
    errors = []
    warnings = []

    text = skill_md.read_text()
    frontmatter = parse_frontmatter(text)
    if frontmatter is None:
        errors.append("missing frontmatter (no leading --- block)")
        return name, skill_dir, errors, warnings

    skill_name = extract_field(frontmatter, "name")
    description = extract_field(frontmatter, "description")

    if not skill_name:
        errors.append("frontmatter missing 'name'")
    if not description:
        errors.append("frontmatter missing 'description'")
    elif len(description) > DESCRIPTION_MAX_LENGTH:
        warnings.append(
            f"description is {len(description)} chars (over {DESCRIPTION_MAX_LENGTH})"
        )

    return name, skill_dir, errors, warnings


def zip_skill(skill_dir, dist_dir):
    dist_dir.mkdir(parents=True, exist_ok=True)
    zip_path = dist_dir / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(skill_dir.rglob("*")):
            if file_path.is_file():
                zf.write(file_path, file_path.relative_to(skill_dir.parent))
    return zip_path


def main():
    if not SKILLS_DIR.is_dir():
        print(f"No skills/ directory found at {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print(f"No SKILL.md files found under {SKILLS_DIR}")
        return 0

    had_errors = False
    for skill_md in skill_files:
        name, skill_dir, errors, warnings = check_skill(skill_md)

        for error in errors:
            print(f"ERROR [{name}]: {error}")
            had_errors = True
        for warning in warnings:
            print(f"WARNING [{name}]: {warning}")

        if not errors:
            zip_path = zip_skill(skill_dir, DIST_DIR)
            print(f"OK [{name}]: packaged -> {zip_path.relative_to(REPO_ROOT)}")

    return 1 if had_errors else 0


if __name__ == "__main__":
    sys.exit(main())
