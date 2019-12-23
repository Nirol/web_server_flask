import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('APP_SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = (os.environ.get('DB_HOSTNAME') or "127.0.0.1") + "/"
    db_name =  os.environ.get('DB_NAME')

    FULL_DB_URL = 'mysql://' + db_username + ":" + db_password + "@" + db_host + db_name

    FLASKY_MAIL_SUBJECT_PREFIX = '[Bukka Blog]'
    FLASKY_MAIL_SENDER = 'Bukka'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.FULL_DB_URL


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = Config.FULL_DB_URL
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir,
    #                                                       'data-tests.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = Config.FULL_DB_URL
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir,
    #                                                       'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
