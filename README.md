# epita-googlenews-seo

## TL;DR

```
    sudo install.sh
    scrapy crawl gnews
    python manage.py runserver
```

## Mettre à jour la BDD

Les tables de la BDD se mettent à jour en fonction des objets définient dans le fichier ```models.py```. Pour applique des motifications faites dans ce fichier  
```
    python manage.py makemigrations
    python manage.py migrate
```

## Links

* [N-grams extraction](http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/)
* [Python case insensitive replace](http://stackoverflow.com/questions/919056/python-case-insensitive-replace)

## DEBUGGING with PyCharm

The script used for debug purpose is ```start.py```  
Follow the instruction of the first answer   http://stackoverflow.com/questions/21788939/how-to-use-pycharm-to-debug-scrapy-projects

## Requirements

* python 2.7 or higher
* [scrapy](http://scrapy.org/)
* [feedparser](https://github.com/kurtmckee/feedparser)

## Coding

You need a python IDE like [PyCharm](https://www.jetbrains.com/pycharm/)


## Running

```scrapy crawl gnews```

## Tests

High tech Google News cluster
Peluche connectée google feed
