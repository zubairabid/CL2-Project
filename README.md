[TOC]

# Sentiment Classification for Bengali News Articles

## How to run this

### Environment

The project is implemented as a Jupyter Notebook. Developed on `Anaconda 4.6.12`. 

`conda list` output is given in [this file](conda-req.txt)

### Dictionary

The dictionary is already saved as a `.pickle` object. If you want to add to it and improve it, then run [this notebook](Final/bn_en_Dict.ipynb)

### Classifier

Run [this notebook](Final/Classifiers.ipynb) for the classifier(s)

## What is Available

### (Unannotated) Dataset

Data from [Kaggle](https://www.kaggle.com/csoham/classification-bengali-news-articles-indicnlp)

Formatted properly as JSON. Files available for

1. [Anandabazar](Final/Datasets/newsarticles/CLEANED/anandabazar_articles_clean.json)
2. [Ebala](Final/Datasets/newsarticles/CLEANED/ebala_articles_cleaner.json)

### Bengali-English word-level Dictionary

Combining scraped results from Google Translate, and [an existing project by Minhas Kamal](https://github.com/MinhasKamal/BengaliDictionary)

### Classifiers

The classifier is available [here](Final/Classifiers.ipynb). It is a notebook, and the report  is included.

### Positive-Negative English Wordlists

Using wordlists compiled [here](https://gist.githubusercontent.com/mkulakowski2/4289437/raw/1bb4d7f9ee82150f339f09b5b1a0e6823d633958/positive-words.txt) and [here](https://gist.githubusercontent.com/mkulakowski2/4289441/raw/dad8b64b307cd6df8068a379079becbb3f91101a/negative-words.txt). I added some words to the lists for completeness.

## Notes

1. The [test directory](tests/) is a compilation of code I was writing with a different directory structure. *None of that code is guaranteed to work*.
2. [Slides used for presentation are available](CL2Project.pdf).

## Paper References

1. Das, Amitava, and Sivaji Bandyopadhyay. "Subjectivity detection in english and bengali: A crf-based approach." *Proceeding of ICON* (2009).
2. Liu, Bing, Minqing Hu, and Junsheng Cheng. "Opinion observer: analyzing and comparing opinions on the web." *Proceedings of the 14th international conference on World Wide Web*. ACM, 2005.