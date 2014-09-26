import requests
import htmldom

from config import config

class Crawler(object):

    def __init__(self):
        pass

    def crawl(self):
        pass

if __name__ == '__main__':
    proxy_sites = config.proxy_sites()

    for ps in proxy_sites:
        print(ps)
