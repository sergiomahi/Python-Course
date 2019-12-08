
import pymongo
from pymongo import MongoClient
import sys
import datetime

print(sys.version)
HOST = 'localhost'
PORT = 27017 # Default port for MongoDB

myClient = MongoClient(HOST, PORT)

# Create the database.
db = myClient.mydb

# Create a collection (table)
users = db.users

user1 = {'username': 'Sergio', 'password': 'secret', 'favorite_number': 9, 'hobbies': ['python', 'games', 'pizza']}

# Insert one document into a collection
user_id = users.insert_one(user1)
print("User {} successfully inserted.".format(user_id.inserted_id))

# Insert multiple documents.

user2 = {'username': 'Culo', 'password': 'secret2'}
user3 = {'username': 'Lyss', 'password': 'secret3'}
new_user = [user2, user3]

users_ids = users.insert_many(new_user)
print("Users {} successfully inserted.".format(users_ids.inserted_ids))

## Count documents.

print("Number of users: {}".format(users.find().count()))
users.find({"favorite_number": 9}).count()
users.find({"favorite_number": 9, "username": 'Culo'}).count()

## Datetime and conditions

current_day = datetime.datetime.now()
print(current_day)

old_date = datetime.datetime(2009,8,11)

user4 = {"username": 'Barto', "date": current_day}
uid = users.insert(user4)

users.find({"date": {"$gt": old_date}}) # gt stands for greater than

users.find({"date": {"$exists": True}}).count()

users.find({"username": {"$ne": "Barto"}}) # ne stands for not equal


## Indexes

db.users.create_index([("username", pymongo.ASCENDING)], unique=True)
users.find({"username": "Culo"}) # That's a faster operation now that we have the index on the username