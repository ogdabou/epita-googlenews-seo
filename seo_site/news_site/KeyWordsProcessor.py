from __future__ import division

from .models import Article
from .stopword import stopWord
from .NGram import NGram
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tag import pos_tag

import math

from .Lemmatizer import penn_to_wn

class KeyWordsProcessor():

    def process(self, feed):
        ngramprocessor = NGram()
        articles = Article.objects.filter(feed_id=feed.id)
        stopWordProcessor = stopWord()
        wnl = WordNetLemmatizer()

        articles_ngrams_list = []
        lemmatized_articles = []
        for article in articles:
            # stop word
            cleaned = stopWordProcessor.stop_little_words(article.description_text)

            # lemm

            taggedWords = pos_tag(cleaned.split(" "))
            lems = []

            # Tagged word form ( "word" , "NNP") but wordnet tags needed
            for taggedWord in taggedWords:
                pos = penn_to_wn(taggedWord[1])
                if pos is not None:
                    lems.append(wnl.lemmatize(taggedWord[0], pos))

            article.lemmatized_description = " ".join(lems)
            # n grams
            article.description_ngrams = ngramprocessor.computeNGrams(lems, 2)
            articles_ngrams_list.append(article.description_ngrams)
            article.lemmatized_description = lems
            article.save()

        # tf-idf des n-grams
        # can be optimized : do not compute for a already-computed ngram
        print "computing tf*idf"

        tf_idfs = []
        for article in articles:
            tf_idf_description_words = []

            # compute number of occurence of most used term
            maxOccurenceInDocument = 0
            for ngram in article.description_ngrams:
                if article.description_ngrams.count(ngram) > maxOccurenceInDocument:
                    maxOccurenceInDocument = article.description_ngrams.count(ngram)

            for ngram in article.description_ngrams:

                tf_idf = tfidf(ngram, article.description_ngrams, articles_ngrams_list, maxOccurenceInDocument)

                print (ngram, tf_idf)
                if not any(ngram in ngram_tf_tuple for ngram_tf_tuple in tf_idfs) and tf_idf != 0.0:
                    tf_idfs.append((ngram, tf_idf))
                    tf_idf_description_words.append((ngram, tf_idf))
            article.tf_idf_description_words = tf_idf_description_words
            article.save()

        print "#######################"
        ngrams_sorted_by_tf_idf = sorted(tf_idfs, key=lambda tup: tup[1], reverse=True)
        print ngrams_sorted_by_tf_idf
        keywords = []


def TermFrequencyInDocument(term, document, maxOccurenceInDocument):
    return float(float(document.count(term)) / float(maxOccurenceInDocument))

# documents are made of ngrams
def InverseDocumentFrequency(term, documents):
    number_of_documents_with_term = 0
    for document in documents:
        if term in document:
            number_of_documents_with_term += 1

    idf = math.log(len(documents) / number_of_documents_with_term) + 1
    return idf

def tfidf(term, document, documents, maxOccurenceInDocument):
    result = TermFrequencyInDocument(term, document, maxOccurenceInDocument) * InverseDocumentFrequency(term, documents)
    print "tfidf ",result, " = ", TermFrequencyInDocument(term, document, maxOccurenceInDocument), " * " , InverseDocumentFrequency(term, documents)
    return result

