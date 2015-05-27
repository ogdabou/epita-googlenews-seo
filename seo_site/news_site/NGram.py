__author__ = 'ogdabou'

class NGram():
    
    # level 2 = Bigram, 3 = Trigrams...
    def computeNGrams(self, text, level):
        words = text.split()
        ngrams = zip(*[words[i:] for i in range(level)])
        print ngrams
        return ngrams

