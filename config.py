import os


class Config:
    '''
    General configuration parent class
    '''
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kate:Kate@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=True


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kate:Kate@localhost/blog'

    DEBUG = True

config_options ={
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig}