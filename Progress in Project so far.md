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









## Off the bat

1. Use sentence level at sentiwordnet
2. If odd number of negations (fix this maybe?) then invert the positive/negative score of the sentence. OR. Look if negation is next to a content word
3. First sentences more important than later (pyramid - use a parabolic curve to grade). Take a weighted average of sentence contributions.
4. Titles do not help much



```python
sentences = body.split('|')
n = len(sentences)

i = 0.1

docscore = [0, 0, 0]
for sentence in sentences:
    
    # senscore keeps track of positive, negative, and objective
    senscore = [0, 0, 0]
    
    j = 0
    neg = 0
    
    for word in sentence:
        if word in stopword:
            continue
        j += 1
        senscore[0] += swn[word].pos_score()
        senscore[1] += swn[word].neg_score()
        senscore[2] += swn[word].obj_score()
    
    	if word in negword:
            neg += 1
    
    # Normalising the score
    senscore[0] /= j
    senscore[1] /= j
    senscore[2] /= j
    
    # Negation application
    if neg % 2 != 0:
        senscore[0], senscore[1] = senscore[1], senscore[0]
      
	# docscore  = weighted average of senscore
    docscore[0] = senscore[0] * e ^ (-i)
    
    i += 0.1
   
```



