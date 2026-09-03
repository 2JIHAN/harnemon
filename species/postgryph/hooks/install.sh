#!/usr/bin/env bash
set -euo pipefail
TARGET_DIR="${1:-.}"
GIT_HOOKS_DIR="$TARGET_DIR/.git/hooks"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -d "$TARGET_DIR/.git" ]; then
  mkdir -p "$GIT_HOOKS_DIR"
  DEST="$GIT_HOOKS_DIR/pre-commit"
  if [ ! -f "$DEST" ]; then
    cp "$SCRIPT_DIR/pre-commit" "$DEST"
    chmod +x "$DEST"
  elif ! grep -q "Postgryph Gate" "$DEST" 2>/dev/null; then
    echo "" >> "$DEST"
    echo "# --- Chained Postgryph Gate Hook ---" >> "$DEST"
    echo "if [ -f \"$SCRIPT_DIR/pre-commit\" ]; then" >> "$DEST"
    echo "  bash \"$SCRIPT_DIR/pre-commit\"" >> "$DEST"
    echo "fi" >> "$DEST"
  fi
  git -C "$TARGET_DIR" config core.hooksPath .git/hooks 2>/dev/null || true
fi
