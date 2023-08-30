/**
	Title: hochdoerfer-assignment4.1-mongoDB-shell
    Author: Kyle Hochdoerfer
    Date: 08/29/23
    Description: List of MongoDB queries that I wrote for this assignment
 */

//Write a query to display all objects stored in the users collection
db.users.find()

//Write a query to display a user with the email of jbach@me.com
db.users.find({"email": "jbach@me.com"})

//Write a query to display a user with the last name of Mozart
db.users.find({"lastName": "Mozart"})

//Write a query to display a user with the first name of Richard
db.users.find({"firstName": "Richard"})

//Write a query to display a user with the employeeId of 1010
db.users.find({"employeeId": "1010"})