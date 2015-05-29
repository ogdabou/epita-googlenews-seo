from __future__ import division

from .models import Article
from .stopword import stopWord
from .NGram import NGram
import Lemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag


import math

from .Lemmatizer import penn_to_wn

class KeyWordsProcessor():
    ngramprocessor = NGram()
    stopWordProcessor = stopWord()

    def processDescriptions(self, feed):
        articles = Article.objects.filter(feed_id=feed.id)
        articles_ngrams_list = []

        cleaned = self.stopWordProcessor.stop_little_words(article.description_text)
        lems = Lemmatizer.lemmatize(cleaned.split(" "))
        article.description_ngrams = self.ngramprocessor.computeNGrams(lems, 2)
        articles_ngrams_list.append(article.description_ngrams)
        article.save()

    def process(self, feed):
        articles = Article.objects.filter(feed_id=feed.id)

        articles_ngrams_list = []
        for article in articles:
            # stop word
            cleaned = self.stopWordProcessor.stop_little_words(article.description_text)

            # lemm
            lems = Lemmatizer.lemmatize(cleaned.split(" "))
            article.lemmatized_description = " ".join(lems)

            # n grams
            article.description_ngrams = self.ngramprocessor.computeNGrams(lems, 2)
            articles_ngrams_list.append(article.description_ngrams)
            article.save()

        # tf-idf des n-grams
        # can be optimized : do not compute for a already-computed ngram
        print "computing tf*idf"

        tf_idfs = []
        for article in articles:
            description_tfidf_list = self.tf_idfs(article.description_ngrams, articles_ngrams_list)
            article.tf_idf_description_words = description_tfidf_list
            tf_idfs += description_tfidf_list
            article.save()

        print "#######################"
        ngrams_sorted_by_tf_idf = sorted(tf_idfs, key=lambda tup: tup[1], reverse=True)
        print ngrams_sorted_by_tf_idf
        keywords = []

    # compute list of ngrams tf-idf on a document
    def tf_idfs(self, document, corpus):
        tfidf_list = []
        maxOccurence = None
        for ngram in document:
            if maxOccurence is None:
                maxOccurence = self.maxOccurence(document)
            tfidf_value = tfidf(ngram, document, corpus, maxOccurence)
            if tfidf_value not in tfidf_list and tfidf_value != 0.0:
                tfidf_list.append((ngram, tfidf_value))
            print (ngram, tfidf_value)
        return tfidf_list

    # document is a list of n-grams
    def maxOccurence(self, document):
        maxOcurrence = 0;
        for ngram in document:
            if document.count(ngram) > maxOcurrence:
                maxOcurrence = document.count(ngram)
        return maxOcurrence


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

