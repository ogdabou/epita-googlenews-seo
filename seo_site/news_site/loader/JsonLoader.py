__author__ = 'ogdabou'

import json
import seo_site.news_site.models.Article


class JsonLoader():

    # loads a json file and returns a dict
    def load(self):
        jsonObject = json.load(open("/home/ogdabou/git/gnews/output.json"))
        jsonObject = jsonObject[0]
        return jsonObject;

    def transform(self, jsonData):
        print "transforming"
        print jsonData
        return ""

jsonR = JsonLoader()
data = jsonR.load()

jsonR.transform(data)