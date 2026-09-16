#!/usr/bin/env python3
"""Rebuild the Aliases table in README.md from the [alias] section of .gitconfig.

Each alias line in .gitconfig is expected to end with a trailing
"# Description" comment, which becomes the Description column. Run this
after adding/editing/removing aliases so the README stays in sync.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GITCONFIG = REPO_ROOT / ".gitconfig"
README = REPO_ROOT / "README.md"

TABLE_HEADER = "| Alias | Command | Description |"
TABLE_DIVIDER = "| --- | --- | --- |"


def parse_aliases(gitconfig_text: str) -> list[tuple[str, str, str]]:
    lines = gitconfig_text.splitlines()
    in_alias_section = False
    aliases = []

    for line in lines:
        stripped = line.strip()
        if re.match(r"^\[.*\]$", stripped):
            in_alias_section = stripped == "[alias]"
            continue
        if not in_alias_section or not stripped:
            continue

        name, _, rest = stripped.partition("=")
        name = name.strip()
        rest = rest.strip()

        comment = ""
        if " # " in rest:
            rest, _, comment = rest.partition(" # ")
            rest = rest.strip()
            comment = comment.strip()

        value = rest.strip('"')
        command = format_command(value)
        description = comment if comment else command
        if description:
            description = description[0].upper() + description[1:]

        aliases.append((name, command, description))

    return aliases


def format_command(value: str) -> str:
    match = re.match(r"^!f\(\)\s*\{\s*(.*?)\s*;?\s*\}\s*;\s*f$", value)
    if match:
        body = match.group(1)
        steps = [s.strip() for s in body.split(";") if s.strip()]
        steps = [re.sub(r"^git\s+", "", s) for s in steps]
        return unescape(" && ".join(steps))

    if value.startswith("!"):
        value = value[1:].strip()
        return unescape(re.sub(r"^git\s+", "", value))

    return unescape(value)


def unescape(text: str) -> str:
    return text.replace('\\"', '"').replace("|", "\\|")


def render_table(aliases: list[tuple[str, str, str]]) -> str:
    rows = [TABLE_HEADER, TABLE_DIVIDER]
    for name, command, description in aliases:
        rows.append(f"| `{name}` | `{command}` | {description} |")
    return "\n".join(rows)


def main() -> None:
    gitconfig_text = GITCONFIG.read_text()
    readme_text = README.read_text()

    aliases = parse_aliases(gitconfig_text)
    table = render_table(aliases)

    marker = "## Aliases\n\n"
    idx = readme_text.find(marker)
    if idx == -1:
        raise SystemExit("Could not find '## Aliases' section in README.md")

    before = readme_text[: idx + len(marker)]
    new_readme = before + table + "\n"

    README.write_text(new_readme)
    print(f"Updated {README} with {len(aliases)} aliases.")


if __name__ == "__main__":
    main()
