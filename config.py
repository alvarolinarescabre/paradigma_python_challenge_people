class Config(object):
   ''' Common configuration '''
   DEBUG = False
   SQLALCHEMY_ECHO = False
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:<passsword>@host/database'

class DevelopmentConfig(Config):
   ''' Development configuration '''
   DEBUG = True
   SQLALCHEMY_ECHO = True
   SQLALCHEMY_TRACK_MODIFICATIONS = True
   
class TestingConfig(Config):
   ''' Testing configuration '''
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:<passsword>@host/database'
   
class ProductionConfig(Config):
   ''' Production configuration '''
   DEBUG = False

app_config = {
   'development' : DevelopmentConfig,
   'production' : ProductionConfig,
   'testing' : TestingConfig,
   'default' : 'development'
}
