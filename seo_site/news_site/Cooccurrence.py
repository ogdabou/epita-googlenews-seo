from .models import Request, Article
import spellCorrector

__author__ = 'Lenjyco'
class Cooccurrence():

    def process(self, requests):
        articles = Article.objects.all()

        for request in requests:
            corrected_request=[]
            for word in request.request.split(" "):
                corrected_request.append(spellCorrector.correct(word))
                print corrected_request
            request.corrected_request = corrected_request
            request.save()

            for article in articles:
                if article.content_ngrams is not None and article.content_ngrams !="":
                    article.content_ngrams = eval(article.content_ngrams)
                    article.tf_idf_text_words = eval(article.tf_idf_text_words)
            request.results = self.compute(articles, corrected_request)
            request.save()


    def compute(self, articles, request):
        usefull_words = self.PickUsefullWord(request, articles)
        counts_request = self.CountRW(request,articles)
        i = 0
        counts_use_request=[]
        highscore_usefulls =[]
        for word in usefull_words:
            count_usefull = self.CountUW(word, articles)
            i = 0
            for word_request in request:
                counts_use_request.append(self.CountUsefullWordRequestWord(word[0][0], word_request, articles))
                highscore_usefulls.append(((word[0][0], word_request), self.Dice(count_usefull, counts_request[i], counts_use_request[i])))
                i += 1
        return self.compute_request_usefull(highscore_usefulls, request)

    def compute_request_usefull(self, hgscore_usefull, request):
        list_max_dice=[]
        max = 0
        for usefull_words in hgscore_usefull:
            if max < usefull_words[1]:
                max = usefull_words[1]
                list_max_dice = []
                list_max_dice.append(usefull_words)
            elif max == usefull_words[1]:
                list_max_dice.append(usefull_words)
        return list_max_dice

    def PickUsefullWord(self, request, articles):
        tf_idfs=[]
        for article in articles:
            for word in request:
                if word in article.content_text:
                    for tf_idf in article.tf_idf_text_words:
                        if tf_idf not in tf_idfs:
                            tf_idfs.append(tf_idf)
        tf_idfs = sorted(tf_idfs, key=lambda tup: tup[1], reverse=True)
        return tf_idfs[:20]

    def CountUW(self, use_word, articles):
        count = 0
        for article in articles:
            if article.lemmatized_text.count(use_word[0][0]) != 0:
                count = count + 1
        return count

    def CountRW(self, request, articles):
        counts = []
        for word in request:
            count = 0
            for article in articles:
                if article.lemmatized_text.count(word) != 0:
                    count = count + 1
            counts.append(count)
        return counts

    def CountUsefullWordRequestWord(self, use_word, request_word, articles):
        count = 0
        for article in articles:
            if article.lemmatized_text.count(use_word) != 0 and article.lemmatized_text.count(request_word) != 0:
                    count = count + 1
        return count

    def Dice(self, count_usefull, count_request, count_use_request):
        return float(float(count_use_request) / (float(count_usefull) + float(count_request)))





