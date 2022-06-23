import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:

    # DB Credentials
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')
    DB_DRIVER = os.environ.get('DB_DRIVER', 'postgresql')

    SQLALCHEMY_DATABASE_URI = f'{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class DevConfig(BaseConfig):
    DEBUG = True

    # Logs
    LOG_LEVEL = 'DEBUG'
    LOG_TYPE = 'file'


class TestConfig(BaseConfig):
    pass
