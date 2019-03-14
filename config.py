import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'x/A?D(G+KbPeShVmYq3s6v9y$B&E)H@M'
    API_KEY = os.environ.get('API_KEY') or 'YFK0BCEEFCC9KARD'
    NEWS_KEY = os.environ.get('NEWS_KEY') or 'ca29302415344c19801654921781efc7'
