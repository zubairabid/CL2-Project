[TOC]

# Progress in Project so far

## What I have:

- Simple Rule-based Sentiment Classifier, custom rules

- Simple Rule-based Sentiment Classifier using SentiWordNet (under construction)

- [Unrelated] A bengali-english dictionary

- [Unrelated] Lots of cleaning scripts

- [Unrelated] A 'bengali sentiwordnet' , need to check for completeness

## Plans

1. Finish a **proper rule-based** sentiment classifier
   1. TODO: Add more words to word list
2. Finish a **rule-based** sentiment classifier with **sentiwordnet**
   1. *Primary issue*: which sentiments to consider
   2. Which words to consider
3. Add a **subjectivity/objectivity score**, and add **more features** to make it more accurate
   1. Which features
4. Code and format a proper Bengali SentiWordNet
5. Clean up and present a nicer Bengali-English word-level Translator

### Outputs

#### Primary

1. A tagger for **bengali news articles**, tagging articles as subjective/objective, and also a positive/neutral/negative polarity score if subjective. 
   1. Cannot demonstrate accuracy as lack of available tagged datasets
   2. Demonstrate cases of work/otherwise
2. Constructed a (small) dataset of tagged data, which can be used in future pipelines.

#### Secondary

1. Bengali SentiWordNet
2. Bengali-English word-level Translator