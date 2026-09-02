#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_DIR="$(git rev-parse --git-dir 2>/dev/null || echo ".git")"

if [ ! -d "$GIT_DIR" ]; then
  echo "⚠️ Not a git repository. Skipping hook installation."
  exit 0
fi

mkdir -p "$GIT_DIR/hooks"
for h in commit-msg pre-commit; do
  if [ -f "$SCRIPT_DIR/$h" ]; then
    cp "$SCRIPT_DIR/$h" "$GIT_DIR/hooks/$h"
    chmod +x "$GIT_DIR/hooks/$h"
    echo "🪝 Installed Git hook: $h"
  fi
done
