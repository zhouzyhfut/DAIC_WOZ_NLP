"""
Author: Joshua Driscol
Date: 04.13.2019

Wrapper methods for NLTK processing. These methods assume that nltk.download() has been run at least once.

Generally each method requires a list (or list of lists) and then returns a processed list.
"""

import string
import nltk


#Input a document and receive a list of lists detailing individual word tokens.
#Note, this is a whitespace tokenizer, which preserves contractions.
def tokenize(doc):
    #return nltk.word_tokenize(doc)
    return nltk.tokenize.WhitespaceTokenizer().tokenize(doc)


#Convert all tokens to lowercase. Assumes that tokenizing has already occurred.
def lower_case(tokens):
     return [token.lower() for token in tokens]


#This method removes NLTK stopwords. Currently, this method works for English stopwords.
#More work can be done to input a "language" parameter to make it more customizable by language.
def remove_stopwords(tokens):
    #Create stopwords set for English.
    #This list can be modified in the english.txt file for NLTK, or use this syntax:
    # stopwords.extend(your_list_here)
    stops = set(nltk.corpus.stopwords.words('english'))

    return [token for token in tokens if token not in stops]


#Remove punctuation and replace it with an empty string character.
#Example: can't --> cant
def strip_punctuation(tokens):
    #Create punctuation list: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    punctuation = string.punctuation

    #See docs: str.maketrans() will make a table to pass to str.translate()
    table = str.maketrans('', '', string.punctuation)

    return [token.translate(table) for token in tokens]


#Strip any non-alphabetic characters.
def remove_numbers(tokens):
    return [token for token in tokens if token.isalpha()]


#TO IMPLEMENT:
#-make this helper function a class
#-part of speech tagging
#-lemmatization
#-stemming
#-others?