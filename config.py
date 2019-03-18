import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'x/A?D(G+KbPeShVmYq3s6v9y$B&E)H@M'
    API_KEY = os.environ.get('API_KEY') or 'YFK0BCEEFCC9KARD'
    NEWS_KEY = os.environ.get('NEWS_KEY') or 'ca29302415344c19801654921781efc7'
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY') or 'dyvovX6kCCZ4CUo33hWYHABWT'
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET') or 's7Csizvn47r5H0a0SmxV5kVniV7f2LN87Hy0f3PiRZIbFUJ89J'
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN') or '4047015314-jX4Gsa4rDgrUTxKvuYFQOnxpE2osHowDEcXx7me'
    ACCESS_SECRET = os.environ.get('ACCESS_SECRET') or 'RsKqOskhksb7wJ2Qed50umhHAmcp66SK9t2fp75m4MOpJ'
    QUANDL_KEY = os.environ.get('QUANDL_KEY') or 'Pz_WG_s6h3rjFppoeKCg'
