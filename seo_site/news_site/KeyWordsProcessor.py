__author__ = 'ogdabou'

from .models import Article
from .stopword import stopWord
from .NGram import NGram

class KeyWordsProcessor():

    def process(self, feed):
        ngramprocessor = NGram()
        articles = Article.objects.filter(feed_id=feed.id)
        stopWordProcessor = stopWord()

        for article in articles:
            # stop word
            cleaned = stopWordProcessor.stop_little_words(article.description_text)


            # lemm

            # n grams
            ngrams = ngramprocessor.computeNGrams(cleaned, 2)
            print ngrams

        # tf-idf des n-grams

        # les meilleurs keywords