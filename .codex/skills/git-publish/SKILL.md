---
name: git-publish
description: Use when committing or pushing changes in this repository. Applies to staging review, semantic commit messages, hook-aware commit workflow, and safe direct pushes when the user explicitly wants them.
---

# Git Publish

Use this skill when the user asks to commit, push, publish, or otherwise finalize repo changes through git.

## Repo-Specific Expectations

- This repo has local hook support installed via `make install-hooks`.
- The generated pre-commit hook blocks commits of:
  - `.env` files
  - `wip/`
  - `_site/`
- For site-affecting changes, the hook runs `make build` before commit.
- `make audit` is the stronger pre-push check when content/config/layouts changed.

## Workflow

1. Inspect `git status --short`.
2. Review the changed files before staging anything.
3. Stage only the files that belong to the requested task.
4. Make sure secrets, `wip/`, and generated output are not staged.
5. If the change touches content, config, layouts, includes, Sass, or assets, run:
   - `make build`
   - `make audit`
6. Write a semantic commit message that describes the real change, not a vague summary.
7. Commit non-interactively.
8. Push only when the user explicitly asks for it, or has clearly authorized it in the current thread.

## Commit Message Rules

- Prefer concise semantic prefixes:
  - `feat:`
  - `fix:`
  - `refactor:`
  - `style:`
  - `docs:`
  - `chore:`
- Use a scope when it improves clarity:
  - `feat(blog): ...`
  - `fix(site): ...`
  - `docs(skills): ...`
- Keep the subject line specific and in the imperative mood.
- Good examples:
  - `feat(blog): sharpen PyFlink social metadata and LinkedIn embed`
  - `fix(site): exclude internal scripts from published output`
  - `docs(skills): codify post-before-social publishing flow`
- Avoid:
  - `updates`
  - `misc fixes`
  - `stuff`
  - `final changes`

## Guardrails

- Never commit `.env`, `_site/`, or `wip/`.
- Never sweep unrelated changes into the same commit just because they are present.
- Do not amend history unless the user explicitly asks.
- Do not use destructive git commands like `reset --hard`.
- If hooks fail, fix the cause rather than bypassing them.
- If push target is ambiguous, prefer the current branch unless the user explicitly says `master` or `main`.
- If the user has explicitly said direct push to `master` is acceptable, that is sufficient authorization for this repo, but still make sure the commit is clean first.

## Output

When finishing a git task, report:

- the commit message used
- whether hooks/build checks passed
- whether the changes were pushed, and to which branch
