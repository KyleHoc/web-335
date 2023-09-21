#-----------------------------------------------------------------------
# Title: hochdoerfer_usersp1.py
# Author: Kyle Hochdoerfer
# Date: 09/18/23
# Description: Code for adding to and updating a collection in MongoDB
#-----------------------------------------------------------------------

#Import MongoClient
from pymongo import MongoClient

#Import datetime
from datetime import datetime

#Import a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.tydee4p.mongodb.net/?retryWrites=true&w=majority")

#Configure a variable to access WEB335DB
db = client["web335DB"]

#Create a composer object literal to store in the database
new_comp = {"firstName": "Joseph", "lastName": "Haydn", "employeeId": "1014", "email": "jhaydn@me.com", "dateCreated": datetime.now()}

#Insert the composer object into the database
db.users.insert_one(new_comp)

#Output the new composer data to demonstrate that it was added to the database
print(db.users.find_one({"lastName": 'Haydn'}))

#Output an empty line to the console
print("")

#Update the email address of the new composer object
db.users.update_one({"firstName":"Joseph"},{"$set":{"email":"haydn@me.com"}})

#Output the new composer data to prove that the email address was changed
print(db.users.find_one({"lastName": 'Haydn'}))

#Output an empty line to the console
print("")

#Delete the new composer data from the database
db.users.delete_one({'firstName':'Joseph'})

#Attempt to print the new composer data to prove that it was deleted
print(db.users.find_one({"lastName": 'Haydn'}))