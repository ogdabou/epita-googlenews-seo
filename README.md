# epita-googlenews-seo

## TL;DR

```
    sudo ./install.sh && ./start.sh
```

## Mettre à jour la BDD

Les tables de la BDD se mettent à jour en fonction des objets définient dans le fichier ```models.py```. Pour appliquer des motifications faites dans ce fichier  
```
    python manage.py makemigrations
    python manage.py migrate
```

## Flush BDD
```
    pyhton manage.py flush
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'root')" | python seo_site/manage.py shell
```

## Links

* [N-grams extraction](http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/)
* [Python case insensitive replace](http://stackoverflow.com/questions/919056/python-case-insensitive-replace)
* [Django] (http://www.django-fr.org/)
* [NLTK] (http://www.nltk.org/)
* [Goose extractor] (https://pypi.python.org/pypi/goose-extractor/)
* [FeedParser] (https://github.com/kurtmckee/feedparser)
* [Automates et dictionnaires](http://www.amazon.com/Automata-Dictionaries-Texts-Computer-Science/dp/190498732X)
* [Automate fini] (http://fr.wikipedia.org/wiki/Automate_fini)
* [Transducteur fini ] (http://fr.wikipedia.org/wiki/Transducteur_fini)


## Fichiers notables du projet
* [Parsing des flux RSS] (https://github.com/ogdabou/epita-googlenews-seo/blob/master/seo_site/news_site/FeedParser.py)
* [Lemmatisation](https://github.com/ogdabou/epita-googlenews-seo/blob/master/seo_site/news_site/Lemmatizer.py)
* [Ngrams](https://github.com/ogdabou/epita-googlenews-seo/blob/master/seo_site/news_site/NGram.py)
* [StopWord](https://github.com/ogdabou/epita-googlenews-seo/blob/master/seo_site/news_site/stopword.py)
* [Correction des requêtes](https://github.com/ogdabou/epita-googlenews-seo/blob/master/seo_site/news_site/spellCorrector.py)
* [Coocurrence](https://github.com/ogdabou/epita-googlenews-seo/blob/master/seo_site/news_site/Cooccurrence.py)
* [Keywords et TF-IDF](https://github.com/ogdabou/epita-googlenews-seo/blob/master/seo_site/news_site/KeyWordsProcessor.py)
