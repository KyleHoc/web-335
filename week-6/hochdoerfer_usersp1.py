#----------------------------------------------------------
# Title: hochdoerfer_usersp1.py
# Author: Kyle Hochdoerfer
# Date: 09/11/23
# Description: Code for writing queries to MongoDB
#----------------------------------------------------------

#Import MongoClient
from pymongo import MongoClient

#Import a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.tydee4p.mongodb.net/?retryWrites=true&w=majority")

#Configure a variable to access WEB335DB
db = client["web335DB"]

#Write a query to store a list of users as a variable
users = (db.users.find({}))

#Print all users to the console
for doc in users:
    print(doc)

#Print an empty line to separate output
print(" ")

#Write a query to display a document where the employee ID is 1011
print(db.users.find_one({"employeeId": '1011'}))

#Write a query to display a document where the lastName is Mozart
print(db.users.find_one({"lastName": "Mozart"}))