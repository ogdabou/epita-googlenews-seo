__author__ = 'ogdabou'

from .models import Article
from .stopword import stopWord
from .NGram import NGram

class KeyWordsProcessor():

    def process(self, feed):
        ngramprocessor = NGram()
        articles = Article.objects.filter(feed_id=feed.id)

        for article in articles:
            # stop word
            cleaned = stopWord.stop_little_words(article.description_text)


            # lemm

            # n grams
            ngrams = ngramprocessor.computeNGrams(article.description_text, 2)

        # tf-idf des n-grams

        # les meilleurs keywords