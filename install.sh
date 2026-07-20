#!/usr/bin/env bash
set -euo pipefail

REPO_RAW_URL="https://raw.githubusercontent.com/96daysleft/git-config/main/.gitconfig"
TMP_CONFIG="$(mktemp)"
trap 'rm -f "$TMP_CONFIG"' EXIT

curl -fsSL -o "$TMP_CONFIG" "$REPO_RAW_URL"

if [ -f "$HOME/.gitconfig" ]; then
  cp "$HOME/.gitconfig" "$HOME/.gitconfig.bak.$(date +%Y%m%d%H%M%S)"
fi

while IFS= read -r -d '' entry; do
  key="${entry%%$'\n'*}"
  value="${entry#*$'\n'}"
  if ! git config --global --get "$key" >/dev/null 2>&1; then
    git config --global "$key" "$value"
  fi
done < <(git config --file "$TMP_CONFIG" --list -z)

echo "Merged into ~/.gitconfig (existing local values were kept, missing keys added)."
echo "If user.name/user.email were just added as placeholders, set your real values:"
echo '  git config --global user.name "Your Name"'
echo '  git config --global user.email "you@example.com"'
