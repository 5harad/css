# Introduction to Python, by example

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/5harad/css/master)

This directory contains materials for the discussion section on introductory Python. The task is to download a text corpus of some sort, split it into words, and proceed to compute the counts of each word. This consists mainly of 2 Jupyter notebooks:
* `IntroToPython.ipynb`: The primary notebook, with the answer cells left blank. Start here.
* `IntroToPython-Suggestions.ipynb`: Same as above, but with instructor answers (suggestions) filled in.

If you don't have [JupyterLab](https://jupyter.org/install) installed, you can use [Binder](https://mybinder.org) (see badge at top of README).

## Bonus challenge

As a follow-up exercise to the introduction, you can try the following exercise: The file `data/top100gutenberg.txt` contains the 100 most popular texts on Project Gutenberg. For each one of these URLs, load the page and locate therein the link to the appropriate `.txt` or `.txt.utf-8` file (this may take a bit of manual inspection at first), download all 100 works to form the text corpus, and then count the occurrences of every word in the corpus.
