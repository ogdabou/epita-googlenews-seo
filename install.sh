#!/bin/bash

# SCRAPY INSTALL

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list
sudo apt-get update && sudo apt-get install scrapy-0.24

# FEEDPARSER INSTALL

git clone https://github.com/kurtmckee/feedparser.git
cd feedparser
sudo python setup.py install
cd ..
sudo rm -rf feedparser

# PIP INSTALL
sudo apt-get install python-pip

# DJANGO INSTALL
sudo pip install Django

# GOOSE EXTRACTOR INSTALL
wget https://pypi.python.org/packages/source/g/goose-extractor/goose-extractor-1.0.25.tar.gz
tar -xvf goose-extractor-1.0.25.tar.gz
cd goose-extractor-1.0.25
sudo python setup.py install
cd ..

#install goose, feedparser, ntlk, goose-extractor
pip install feedparser
pip install nltk
pip install goose-extractor
pip install beautifulsoup

# NLTK DATA DOWNLOAD
sudo mkdir seo_site/nltk_data
sudo python -m nltk.downloader -d seo_site/nltk_data maxent_treebank_pos_tagger punkt wordnet

