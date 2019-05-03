# Sentiment Analysis in Bengali

## Related work

1. [Classification model using ConvNets, reported 99.87% accuracy. ICCIT, 2017](https://ieeexplore.ieee.org/document/8281840)
   Looks scammy af. WTAF is the 

   ```
   Among the comments, 500 comments are positive and the rests are negative. But as the amount of comments is not sufficient to train our proposed network, we just copy-paste the comments repeatedly to increase the size of our dataset.
   ```

   

2. [Tweet Classification in multiple languages](https://www.inf.uni-hamburg.de/en/inst/ab/lt/publications/2015-kumar-etal-mike.pdf)
   SVM using n-grams and SentiWordNet Features. Also Lexical Acquisition, and Distributional Thesaurus.

3. [Sentiment analysis in Bengali Microblogging sites](http://dspace.bracu.ac.bd/xmlui/handle/10361/2902)

4. [More sentiment analysis with some manual dataset](https://pdfs.semanticscholar.org/6d1f/47c985d5d946abcc8c48ec0b8a902f58b960.pdf)

5. [Someone's final project, a jupyter notebook for sentiment analysis in Bangla](https://github.com/abhie19/Sentiment-Analysis-Bangla-Language/blob/master/ANLP%20Final%20Project.ipynb)
   There's a lot of stuff I'll have to clean here, but as far as it goes the closest I have to a proper solution because code is available. As is the data. 

## Computation Resources for Bengali NLP work

1. [spacy.io bengali toolkit](https://github.com/explosion/spaCy/tree/master/spacy/lang/bn)
2. [Unofficial BanglaKit spacy models](https://github.com/banglakit/spacy-models)
3. [BanglaKit awesome-bangla](https://github.com/banglakit/awesome-bangla)

### Datasets

1. [Book data](~/Documents/Acads/Projects/CL2-Project/datasets/books/)
2. [IndicNLP - Newspaper articles](~/Documents/Acads/Projects/CL2-Project/datasets/news-indicnlp/)

## What I've done so far

### Dataset

Bengali News dataset: from leading newspapers

### Preprocessing

- Tokenized

### Sentiment Classification

#### Current Idea

Rule based mechanism:

1. Identify 'Positive' and 'Negative' tokens
2. Identify negators 'na' and invert sentiment accordingly  

Based on these rules, classify texts as positive, negative, neutral. Using only obvious keywords, cannot incorporate more complex features like **metaphor**, or **chaining of keywords to display intent**, or anything of the sort.



