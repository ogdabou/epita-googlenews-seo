__author__ = 'ogdabou'

from .models import Article
from .stopword import stopWord
from .NGram import NGram
from nltk.stem import WordNetLemmatizer
from nltk.tag.api import TaggerI
from nltk.tag import pos_tag

from .Lemmatizer import penn_to_wn

class KeyWordsProcessor():

    def process(self, feed):
        ngramprocessor = NGram()
        articles = Article.objects.filter(feed_id=feed.id)
        stopWordProcessor = stopWord()
        wnl = WordNetLemmatizer()

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

            # n grams

            ngrams = ngramprocessor.computeNGrams(lems, 2)
            print ngrams

        # tf-idf des n-grams

        # les meilleurs keywords