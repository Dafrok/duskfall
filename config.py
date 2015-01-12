# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wangwangwang'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #DUSKFALL_MAIL_SUBJECT_PREFIX = '[DuskFall]'
    #DUSKFALL_MAIL_SENDER = 'Dusk Fall <wshmelo@gmail.com>'
    DUSKFALL_ADMIN = os.environ.get('DUSKFALL_ADMIN')

    @classmethod
    def init_app(cls, app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:@localhost:3308/duskfall'
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config  = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
