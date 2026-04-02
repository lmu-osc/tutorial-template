# Tutorial Template

This repository is a starter template for Quarto-based OSC tutorials.

## Adapting This Template After You Copy It

Use this checklist when creating a new tutorial repository from this template.

1. Update tutorial metadata in `_quarto.yml`.
2. Replace placeholder content in `index.qmd` and `about.qmd`.
3. Rename or replace `TOPIC1/` and `TOPIC2/` folders and their `.qmd` pages.
5. Edit `CITATION.cff` with real authors, affiliations, ORCIDs, and ROR IDs.
6. Review `LICENSE.md` and `LICENSE-CODE.md` to confirm they match your project.
7. The `matomo-analytics.html` file will be managed by OSC staff members--please open a GitHub issue to have this filled out.
8. If your project makes use of R packages, please consider using {renv} for package management. This may be necessary for the GitHub Action to deploy your website.

## Conventions

### File and Folder Naming

Please use lowercase letters only, and no numbers in your file names. To separate words, use kebab case i.e. `hello-there`.

```
# good file name
/somet-topic/some-description.qmd
```

## Build And Preview

Run this to preview the site locally:

```bash
quarto preview
```

## Validate `CITATION.cff`

This repo includes a GitHub Action that validates `CITATION.cff` on push.
You can also validate locally:

```bash
python3 -m pip install --user cffconvert
docker run --rm -v "${PWD}:/app" citationcff/cffconvert --validate
```
