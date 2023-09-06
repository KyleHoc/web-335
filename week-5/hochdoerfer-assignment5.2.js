/**
	Title: hochdoerfer-assignment5.2
    Author: Kyle Hochdoerfer
    Date: 09/5/23
    Description: MongoDB queries for assignment 5.2
 */

    //Insert a document to the composer database containing data for Franz Schubert
    db.users.insertOne({"firstName": "Franz", "lastName": "Schubert", "employeeId": "1013", "email": "fschubert@me.com", "dateCreated": new Date() })

    //Update the document containing the lastName with the value of "Mozart" so that the email is mozart@me.com
    db.users.updateOne({"lastName": "Mozart"}, {$set: {"email": "mozart@me.com"}})

    //Find the document with the changed email to demonstrate that the update operation was successful
    db.users.find({"email": "mozart@me.com"})

    //Display a list of all documents in the collection, showing only the firstName, lastName, and email fields
    db.users.aggregate( [ { $project : { "_id": 0, "firstName": 1 , "lastName": 1, "email": 1 } } ] )