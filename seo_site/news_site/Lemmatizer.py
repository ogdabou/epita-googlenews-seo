__author__ = 'ogdabou'

import math
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

wnl = WordNetLemmatizer()

# lemmatize a list of words
def lemmatize(words):
    taggedWords = pos_tag(words)
    lems = []
    for taggedWord in taggedWords:
            pos = penn_to_wn(taggedWord[1])
            if pos is not None:
                lems.append(wnl.lemmatize(taggedWord[0], pos))
    return lems


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None
