#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
GIT_DIR="$ROOT_DIR/.git"
HOOKS_DIR="$GIT_DIR/hooks"
MARKER="# installed-by-christos-site-hook-setup"

install_pre_commit() {
  cat > "$HOOKS_DIR/pre-commit" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

# installed-by-christos-site-hook-setup

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

STAGED="$(git diff --cached --name-only --diff-filter=ACMR)"

if [[ -z "$STAGED" ]]; then
  exit 0
fi

if echo "$STAGED" | grep -E '^(\.env($|\.)|wip/|_site/)' >/dev/null; then
  echo "Blocked commit: do not commit .env files, wip/ files, or _site/ output." >&2
  exit 1
fi

if echo "$STAGED" | grep -E '^(_config\.yml|404\.html|feed\.xml|content/|_layouts/|_includes/|_sass/|assets/)' >/dev/null; then
  echo "Running site build before commit..." >&2
  make build >/dev/null
fi
EOF
  chmod +x "$HOOKS_DIR/pre-commit"
}

remove_pre_commit() {
  if [[ -f "$HOOKS_DIR/pre-commit" ]] && grep -F "$MARKER" "$HOOKS_DIR/pre-commit" >/dev/null; then
    rm -f "$HOOKS_DIR/pre-commit"
    echo "Removed generated pre-commit hook."
  fi
}

main() {
  local action="${1:-install}"

  if [[ ! -d "$GIT_DIR" ]]; then
    echo "No .git directory found at $ROOT_DIR" >&2
    exit 1
  fi

  mkdir -p "$HOOKS_DIR"

  case "$action" in
    install)
      install_pre_commit
      echo "Installed local git hooks into $HOOKS_DIR"
      ;;
    remove)
      remove_pre_commit
      ;;
    *)
      echo "Usage: $0 [install|remove]" >&2
      exit 1
      ;;
  esac
}

main "$@"
