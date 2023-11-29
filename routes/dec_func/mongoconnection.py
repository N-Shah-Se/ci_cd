from pymongo import MongoClient
from .secret_info import *

client = MongoClient(
    host=HOST,
    port=PORT
)

db_user = client['users']












