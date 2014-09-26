import requests
import htmldom

from config import config

if __name__ == '__main__':
    proxy_sites = config.proxy_sites()

    for ps in proxy_sites:
        print(ps)
