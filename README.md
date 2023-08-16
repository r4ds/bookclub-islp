# R4DS Introduction to Statistical Learning Using Python Book Club

Welcome to the R4DS Introduction to Statistical Learning Using Python Book Club!

We are working together to read [_Introduction to Statistical Learning Using Python_](https://www.statlearning.com) by Gareth James, Daniela Witten, Trevor Hastie, Rob Tibshirani, and Jonathan Taylor (Springer Science+Business Media, LLC, part of Springer Nature, copyright 2023, 978-3-031-38747-0).
Join the [#book_club-islp](https://rfordatascience.slack.com/archives/C05K1HJEXFA) channel on the [R4DS Slack](https://r4ds.io/join) to participate.
As we read, we are producing [notes about the book](https://r4ds.github.io/bookclub-islp/).

## Meeting Schedule

If you would like to present, please see the sign-up sheet for your cohort (linked below, and pinned in the [#book_club-islp](https://rfordatascience.slack.com/archives/C05K1HJEXFA) channel on Slack)!

- [Cohort 1](https://docs.google.com/spreadsheets/d/1mBCB3LM4GkCGvJuAGF12rUyyW1srk6fLjSzQvT0KuC0/edit?usp=sharing) (started 2023-08-13): [Sundays, noon CST/CDT](https://www.timeanddate.com/worldclock/converter.html?iso=20230813T170000&p1=24&p2=1440) | [meeting videos](https://youtube.com/playlist?list=PL3x6DOfs2NGgqCo62O0lDTcJLvGpyG8_g)

<hr>

## How to Present

This repository is made with [Quarto](https://quarto.org/).

To present, follow these instructions:

Do these steps once (steps need to be adapted somewhat for Python/Quarto still):

1. [Setup Git and GitHub to work with RStudio](https://github.com/r4ds/bookclub-setup) (click through for detailed, step-by-step instructions; I recommend checking this out even if you're pretty sure you're all set).
2. Fork and clone this repository to your local computer.
3. Install [Quarto](https://quarto.org/docs/get-started/) and follow the Get Started chapter.

Do these steps each time you present another chapter:

1. Open your project for this book.
2. Create a new file in the folder. For example, to create a new file called `01_exercises.qmd`, navigate to the folder then run `touch 01_exercises.qmd` in the Terminal. 
3. Write in what you would like in the file.
4. Then, in the `_quarto.yml` file, under chapters, add a section with your chapter. The file listed after `part` is the first page of chapter; the ones under chapters will be subpages.

```
  - part: 01_main.qmd
      chapters: 
      - 01_notes.qmd
      - 01_video.qmd
      - 01_exercises.qmd
```

5. Once you have added and edited your files, don’t forget to render the book. Run this in the terminal:

```
quarto render --to html
```

Once you are ready to finalize your changes:

1. Commit your changes.
2. Push your changes to your forked repo and then create a pull request for the R4DS admins to merge your changes.
3. (If they request changes, make them)
4. When your PR has been accepted ("merged"), close out your branch and prepare your local repository for future work.

## On Using Quarto

Quarto is an open-source scientific and technical publishing system built on Pandoc.

You can weave together narrative text and code to produce elegantly formatted output. Quarto documents are fully reproducible. You can use plain `.md` files, Quarto `.qmd`, or Jupyter `.ipynb` files. Check out the files under Examples to see the various options.
