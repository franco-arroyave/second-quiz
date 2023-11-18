from config.db import conexion

class Config:
    cnx = conexion()
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ('mysql+pymysql://'+
                               cnx['user']+':'+
                               cnx['password'] + '@'+
                               cnx['host']+':3306/'+
                               cnx['db'])
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass