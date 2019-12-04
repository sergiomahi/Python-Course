
import pymongo
from pymongo import MongoClient
import sys


print(sys.version)
HOST = 'localhost'
PORT = 27017 # Default port for MongoDB

myClient = MongoClient(HOST, PORT)

# Create the database.
db = myClient.mydb

# Create a collection (table)
users = db.users

user1 = {'username': 'Sergio', 'password': 'secret', 'favorite_number': 9, 'hobbies': ['python', 'games', 'pizza']}

user_id = users.insert_one(user1)
print("User {} successfully inserted.".format(user_id))
