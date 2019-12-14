import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codesoldier
        self.Users = self.db.users

    def insert_user(self, data):
        hash = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.Users.insert({"username": data.username, "name": data.fullname, "password": hash, "email": data.email})

        print("uid is {}".format(id))
        my_user = self.Users.find_one({"username": data.username})

        if bcrypt.checkpw("avocado1".encode(), my_user["password"]):
            print("Matches")