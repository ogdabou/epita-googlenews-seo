# -*- coding: utf-8 -*-

# Scrapy settings for gnews project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gnews'

SPIDER_MODULES = ['gnews.spiders']
NEWSPIDER_MODULE = 'gnews.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gnews (+http://www.yourdomain.com)'
