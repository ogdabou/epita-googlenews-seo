__author__ = 'ogdabou'

class NGram():
    
    # level 2 = Bigram, 3 = Trigrams...
    def computeNGrams(self, text, level):
        if text != None and text != "":
            ngrams = zip(*[text[i:] for i in range(level)])

            print ngrams
            return ngrams
        else:
            return None

