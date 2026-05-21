# Tutorial Template

This repository is a starter template for Quarto-based OSC tutorials. It provides a simple, accessible structure you can copy and adapt to publish a small course or tutorial website.

## Quick overview

- **Purpose:** A lightweight Quarto site template pre-configured for OSC (Open Science Center) tutorials.
- **Who it's for:** educators and researchers who want an easy-to-edit website using Quarto; no deep web development experience required.

## Structure Overview

Top-level files and directories you'll commonly interact with:

- `_quarto.yml` — Site configuration (title, navigation, output settings, theme). Update this to change the site title, navigation order, or basic site settings. We already have a multitude of presets in place here, but feel free to look at Quarto's documentation for further options.
- `index.qmd` — The site homepage content i.e. the landing page when someone opens the link to the tutorial. This should generally be an overview of the tutorial + necessary software information.
- `about.qmd` — An example about page for your tutorial. It's main role is to contain License, Citation, and Contributor information.
- `CITATION.cff` — Citation metadata for your project (authors, affiliations, ORCID, etc.). See the official  [CITATION.cff](https://citation-file-format.github.io/) documentation or sent an OSC member a message if it's unclear how to fill this in.
- `LICENSE.md` and `LICENSE-CODE.md` — License text for content and code respectively. We use CC-BY-SA 4.0 and CC0 1.0 Universal for authored content and code, respectively.
- `lmu-osc-custom.scss` — Site-specific CSS tweaks; add branding or small visual changes here.
- `matomo-analytics.html` — Analytics snippet (managed by OSC staff; do not edit unless instructed).
- `assets/` — Images, downloads, and other static files used by the site.
- `topic-one/`, `topic-two/`, ... — Example topic folders containing `.qmd` pages for tutorial sections. Replace or rename these to match your content.
- `_site/` — Generated site files (output). You normally do not edit this folder directly — it's produced when you build the site.

If you want to change what appears in the site's navigation, edit the `navigation:` section in `_quarto.yml`.

## Adapt this template (practical, plain-language steps)

These instructions are written for less-technical users. You can do most work through the GitHub website or a simple text editor. Developers may prefer the command line.

1) Make a copy of this template

- Use the GitHub "Use this template" button, or ask your organization to create a new repository from this template.

2) Update basic site information

- Open `_quarto.yml` and change the `title:` to your tutorial name. You can edit this file in GitHub's web editor or your local editor.

3) Edit the homepage and about page

- Open `index.qmd` to change the welcome message and overview.
- Open `about.qmd` to add contact info, acknowledgements, and contributor names.

4) Rename or replace example topics and pages

- Replace the example folders like `topic-one/` with folders that match your tutorial sections. Each folder contains `.qmd` files — these are the pages visitors will read.
- The start of each section or new chapter should be the `index.qmd` file *within the relevant directory*. Other pages in the directory would be the chapters of the section. You can think of these index pages as landing pages for a broader category. If you don't need chapters within the section, however, then it is completely acceptable to just use the index page.
- To add a new page: create a new `.qmd` file (for example `topic-three/page-one.qmd`) and include a title at the top of the file:

```
---
title: "My page title"
---

Your content here.
```

5) Add images and files

- Put images or downloadable files in `assets/` (for example `assets/images/logo.png`) and reference them in a page with `![](/assets/images/logo.png)`.

6) Make small style changes

- Use `lmu-osc-custom.scss` for simple visual tweaks (colors, font sizes). For most users, this is optional — only edit if you know basic CSS or want help from a web-savvy colleague.

7) Update project metadata and licensing

- Edit `CITATION.cff` with author names and affiliations so others can cite your tutorial. If you aren't sure what to put, ask collaborators for their preferred name and ORCID.
- Confirm `LICENSE.md` and `LICENSE-CODE.md` reflect how you want to allow reuse of your content and code.

8) Preview your site locally (optional, for people who want to test changes first)

- Install Quarto: follow the instructions at https://quarto.org/docs/get-started/
- From the project folder, run:

```bash
quarto preview
```

- This command opens a local preview in your browser showing how the site will look.

9) Publish changes

Background: we use GitHub Pages to host these repos as live websites, and we rely on an automated pipeline to render any and all of the Qmd, HTML, CSS, etc. files in this repo to the final website. This pipeline should be activated at the beginning of repo usage using this command:

```bash
quarto publish gh-pages
```

This may take several minutes to run, but you can check the Actions tab within the repo to see progress. If you run into problems, however, feel free to contact an OSC staff member.

After this initial set-up, changes you make to the Quarto files and push to GitHub will automatically be reflected in the live website.

(Note: if the repo is private, GitHub Pages cannot be activated.)


10) Need help?

- Open a GitHub issue in your repository describing the change you want and someone from OSC or your team can help. If you prefer direct assistance, share which file you want edited and what text should be added or replaced.

### Running Actions (for non-technical contributors)

This template has several automations in place to help ensure consistency across our repositories, namely a citation file checker, a filename checker, and an automation for publishing the site. You can see details at `.github/workflows/README.md` if interested, but it's not required to know these details by any means.

- If you need to run a repository workflow (for example to re-render the site), open this repository on GitHub and click the **Actions** tab.
- Select the workflow you want (examples: "Render Quarto Site", "Check CITATION.cff", "Filename Checks").
- Click **Run workflow**, and then select the branch you want to test a workflow on from the "Branch:" dropdown. Then click **Run workflow** again to start it.
- After the workflow starts, you can monitor progress on the same page and inspect step logs if something fails. If you are unsure what to do after a failure, open a GitHub issue and paste the error or screenshot.
- If you do not see the **Run workflow** button, you can still make changes by editing files and pushing them to GitHub; the workflows that trigger on `push` will run automatically.

## Conventions and tips

- File names: lowercase and kebab-case (e.g. `my-topic/my-page.qmd`).
- Content: use plain text and simple Markdown/Quarto; avoid embedding complex web widgets unless needed.
- Collaboration: edit content on GitHub using branches and pull requests so teammates can review changes.

## Build And Preview (developer-friendly)

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
