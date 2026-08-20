# CV Variants

Role-specific CV variants are grouped by capture/build month:

```text
variants/
  YYYY/
    MM/
      role-slug/
        cv.tex
        cv.pdf
        _role-context/
```

Use the role context capture date when available. If a variant has no role context, use the month the variant was created.

For a variant at `variants/YYYY/MM/role-slug/cv.tex`, use:

- `\documentclass[]{../../../../friggeri-cv}`
- `\graphicspath{ {../../../../images/} }`

This keeps older application material easy to archive or delete by month without touching the canonical CV at `cv/latex/cv.tex`.
