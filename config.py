import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING')

    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTHORITY = "https://login.microsoftonline.com/common"
    SCOPE = ["User.Read"]
