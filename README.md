# R4DS Python for Data Analysis Book Club

Welcome to the R4DS Python for Data Analysis Book Club!

We are working together to read [_Python for Data Analysis_](https://wesmckinney.com/book/) by Wes McKinney (O'Reilly Media, Inc., copyright 2022, [9781098104030](https://www.oreilly.com/library/view/python-for-data/9781098104023/)).
Join the [#book_club-py4da](https://rfordatascience.slack.com/archives/C03P2J90L30) channel on the [R4DS Slack](https://r4ds.io/join) to participate.
As we read, we are producing [notes about the book](https://r4ds.io/py4da).

## Meeting Schedule

If you would like to present, please see the sign-up sheet for your cohort (linked below, and pinned in the [#book_club-py4da](https://rfordatascience.slack.com/archives/C03P2J90L30) channel on Slack)!

- Cohort 1 (started 2022-08-05, finished 2022-11-11): [meeting videos](https://www.youtube.com/playlist?list=PL3x6DOfs2NGh7IQIQ_pXNkjLVKa-7lgCw)

<hr>

## How to Present

This repository is made with [Quarto](https://quarto.org/).

To present, follow these instructions:

Do these steps once:

* [Setup Github Locally](https://www.youtube.com/watch?v=hNUNPkoledI) (also see [_Happy Git and GitHub for the useR_](https://happygitwithr.com/github-acct.html))
* Fork and clone this repository to your local computer.
* Install [Quarto](https://quarto.org/docs/get-started/) and follow the Get Started chapter.

Do these steps each time you present another chapter:

* Open your project for this book.
* Create a new file in the folder. For example, to create a new file called `01_exercises.qmd`, navigate to the folder then run `touch 01_exercises.qmd` in the Terminal. 
* Write in what you would like in the file.
* Then, in the `_quarto.yml` file, under chapters, add a section with your chapter. The file listed after `part` is the first page of chapter; the ones under chapters will be subpages.

```
  - part: 01_main.qmd
      chapters: 
      - 01_notes.qmd
      - 01_video.qmd
      - 01_exercises.qmd
```

* Once you have added and edited your files, don’t forget to render the book. Run this in the terminal:

```
quarto render --to html
```

Once you are ready to finalize your changes:

* Commit your changes.
* Push your changes to your forked repo and then create a pull request for the R4DS admins to merge your changes.
* (If they request changes, make them)
* When your PR has been accepted ("merged"), close out your branch and prepare your local repository for future work.

## On Using Quarto

Quarto is an open-source scientific and technical publishing system built on Pandoc.

You can weave together narrative text and code to produce elegantly formatted output. Quarto documents are fully reproducible. You can use plain `.md` files, Quarto `.qmd`, or Jupyter `.ipynb` files. Check out the files under Examples to see the various options.
