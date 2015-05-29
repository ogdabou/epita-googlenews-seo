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
        self.compute(articles, corrected_request)


    def compute(self, articles, request):
        usefull_words = self.PickUsefullWord(request, articles)
        print usefull_words
        counts_request = self.CountRW(request,articles)
        i = 0
        counts_use_request=[]
        highscore_usefulls =[]
        hgscore_word = []
        hgscore_words = []
        for word in usefull_words:
            count_usefull = self.CountUW(word, articles)

            for word_request in request:
                print self.CountUsefullWordRequestWord(word, word_request, articles)
                counts_use_request.append(self.CountUsefullWordRequestWord(word, word_request, articles))
                highscore_usefulls.append(self.Dice(count_usefull,counts_request[i],counts_use_request[i]))
                hgscore_word.append(word + word_request)
                hgscore_word.append(highscore_usefulls[i])
                #highscore_usefulls.sort(reverse=True)
            hgscore_words.append(hgscore_word)
        return self.compute_request_usefull(hgscore_words, request)

    def compute_request_usefull(self, hgscore_usefull, request):
        for usefull_words in hgscore_usefull:
            print request
            print "OOOOOOOOOOOOOOOOOOOOOOOOOO"
            print usefull_words[0]

    def PickUsefullWord(self, request, articles):
        tf_idfs=[]
        print len(articles)
        for article in articles:
            for word in request:
                if word in article.content_text:
                    for tf_idf in article.tf_idf_text_words:
                        print article.tf_idf_text_words
                        if tf_idf not in tf_idfs:
                            tf_idfs.append(article.tf_idf_text_words)
        tf_idfs.sort(reverse=True)
        return tf_idfs[:20]

    def CountUW(self, use_word, articles):
        for article in articles:
            count = 0
            if article.content_text.count(use_word) != 0:
                count = count + 1
        return count

    def CountRW(self, request, articles):
        counts = []
        for word in request:
            count = 0
            for article in articles:
                if article.content_text.count(word) != 0:
                    count = count + 1
            counts.append(count)
        return counts

    def CountUsefullWordRequestWord(self, use_word, request_word, articles):
        count = 0
        for article in articles:
            if article.content_text.count(use_word) != 0 and article.content_text.count(request_word):
                count = count + 1
        return count

    def Dice(self, count_usefull, count_request, count_use_request):
        return float(count_use_request / (count_usefull + count_request))





