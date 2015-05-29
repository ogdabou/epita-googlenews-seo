from nltk.tokenize import word_tokenize

class stopWord:
    
    def stop_little_words(self, chaine):
        stop_word = ["a","able","about","across","after","all","almost","also","am","among",
                     "an","and","any","are","as","at","be","because","been","but","by","can",
                     "cannot","could","dear","did","do","does","either","else","ever","every",
                     "for","from","get","got","had","has","have","he","her","hers","him","his",
                     "how","however","i","if","in","into","is","it","its","just","least","let","like",
                     "likely","may","me","might","most","must","my","neither","no","nor","not","of","off",
                     "often","on","only","or","other","our","own","rather","said","say","says","she",
                     "should","since","so","some","than","that","the","their","them","then","there",
                     "these","they","this","tis","to","too","twas","us","wants","was","we","were",
                     "what","when","where","which","while","who","whom","why","will","with","would","yet",
                     "you","your","ain't","aren't","can't","could've","couldn't","didn't","doesn't",
                     "don't","hasn't","he'd","he'll","he's","how'd","how'll","how's","i'd","i'll",
                     "i'm","i've","isn't","it's","might've","mightn't","must've","mustn't","shan't",
                     "she'd","she'll","she's","should've","shouldn't","that'll","that's","there's",
                     "they'd","they'll","they're","they've","wasn't","we'd","we'll","we're","weren't",
                     "what'd","what's","when'd","when'll","when's","where'd","where'll","where's","who'd",
                     "who'll","who's","why'd","why'll","why's","won't","would've","wouldn't","you'd",
                     "you'll","you're","you've", ]

        stop_punct = [ ".", "'", "`", "\"", "[", "]", "(", ")", "{", "}", "(", ")", "!", "?", ";", ",", ]

        words = word_tokenize(chaine)
        for word in stop_word:
            if word in chaine:
                #chaine = chaine.remove(word);
                chaine = chaine.replace(" " + word + " ", " ")

        for punct in stop_punct:
            if punct in chaine:
                #chaine = chaine.remove(word);
                chaine = chaine.replace(punct + " ", " ")

        return chaine;
    
#chaine = "The TreeTagger is a tool for annotating text with part-of-speech and lemma information. It was developed by Helmut Schmid in the TC project at the Institute for Computational Linguistics of the University of Stuttgart. The TreeTagger has been successfully used to tag German, English, French, Italian, Dutch, Spanish, Bulgarian, Russian, Portuguese, Galician, Chinese, Swahili, Slovak, Latin, Estonian, Polish and old French texts and is adaptable to other languages if a lexicon and a manually tagged training corpus are available. ";
#test_stop_word = stopWord();
#chaine = test_stop_word.stop_little_words(chaine);
#print "chaine %s :" % chaine;
    
        
    
        