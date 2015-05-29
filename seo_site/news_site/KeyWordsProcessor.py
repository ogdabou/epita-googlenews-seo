__author__ = 'ogdabou'

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
            for ngram in article.description_ngrams:
                tf_idf = tfidf(ngram, article.description_ngrams, articles_ngrams_list)
                print (ngram, tf_idf)
                if not any(ngram in ngram_tf_tuple for ngram_tf_tuple in tf_idfs) and tf_idf != 0.0:
                    tf_idfs.append((ngram, tf_idf))
                    tf_idf_description_words.append(tf_idfs)
            article.tf_idf_description_words = tf_idf_description_words
            article.save()

        print "#######################"
        ngrams_sorted_by_tf_idf = sorted(tf_idfs, key=lambda tup: tup[1], reverse=True)
        print ngrams_sorted_by_tf_idf
        keywords = []


        # les meilleurs keywords


def tf(ngram, text_ngrams):
    return text_ngrams.count(ngram) / len(ngram)

def n_containing(ngram, text_ngrams_list):
    return sum(1 for text_ngrams in text_ngrams_list if ngram in text_ngrams)

def idf(ngram, text_ngrams_list):
    return math.log(len(text_ngrams_list) / (1 + n_containing(ngram, text_ngrams_list)))

def tfidf(ngram, text_ngrams, text_ngrams_list):
    return tf(ngram, text_ngrams) * idf(ngram, text_ngrams_list)