from .models import Article


__author__ = 'ogdabou'

import json


class JsonLoader():

    # loads a json file and returns a dict
    def load(self):
        jsonObject = json.load(open("/home/ogdabou/git/gnews/output.json"))
        jsonObject = jsonObject[0]
        return jsonObject

    def transform(self, jsonData):
        articles = []
        for articleJson in jsonData["articles"]:
            article = Article()
            article.title_text = articleJson["title"]
            article.description_text = articleJson["summary"]
            articles.append(article)
        return articles