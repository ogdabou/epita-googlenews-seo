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
