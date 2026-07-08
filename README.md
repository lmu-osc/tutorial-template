# Tutorial Template

This repository is a starter template for Quarto-based OSC tutorials. It provides a simple, accessible structure you can copy and adapt to publish a small course or tutorial website.

## Primary Documentation

This README only serves as a brief documentation page. Details of the repo and how to adapt it for other tutorials can be found at our publicly-available manual in the [Authoring Tutorials for the OSC](https://lmu-osc.github.io/manual/authoring-tutorials/) section and at the [README-template.md].

## Quick overview

- **Purpose:** A lightweight Quarto site template pre-configured for OSC (Open Science Center) tutorials.
- **Who it's for:** educators and researchers who want an easy-to-edit website using Quarto; no deep web development experience required.


### Quick Start!

Assuming you are a member of the lmu-osc GitHub Organization, you will likely have the rights to create new repos in our org. In particular, you can create new repos from an existing template i.e. using the `tutorial-template` repo. Choose this option when creating your new repo, and follow these instructions:

```bash
quarto use template lmu-osc/tutorial-template
# if you created the project into a subfolder, then run: 
# cd YOUR-FOLDER
```

Next, we want to rename two of the files, `CITATION-template.cff` and `README-template.md`, to the names they should actually have. (The actual `tutorial-template` repo has these files of its own, but the contents are not copied to templates because, well, that repo needs its own CITATION and README files!)

```bash
mv CITATION-template.cff CITATION.cff
mv README-template.md README.md
```

And fially, we can preview everything by running:

```bash
quarto preview
```

Optional: get your website deployed right away (only works for public repos):

```bash
quarto publish gh-pages
```

This may take several minutes to run, but you can check the Actions tab within the repo to see progress. If you run into problems, however, feel free to contact an OSC staff member. Read our documentation on [Activating GitHub Pages](https://lmu-osc.github.io/manual/authoring-tutorials/finalization-and-publishing.html#activate-github-pages-one-time-setup).

