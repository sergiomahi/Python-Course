
# Installation on IOS

Updated December 2019.

Open a new terminal and type:

1. ```bash brew update```
2. brew tap mongodb/brew
3. brew install mongodb-community
4. brew start services mongodb-community


--- If you want to connect a to Mongo you have to do: client = MongoClient(localhost, 27017) wherw MongoClient(host, port)
            or we can aldo use MongoClient('mongodb://localhost:27017/') which is a url.

