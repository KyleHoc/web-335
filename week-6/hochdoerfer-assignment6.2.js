/**
	Title: hochdoerfer-assignment6.2
    Author: Kyle Hochdoerfer
    Date: 09/12/23
    Description: MongoDB queries for assignment 6.2
 */

    //Display a the list of documents in the houses collection
    db.houses.find({})

    //Display a list of documents in the students collection
    db.students.find({})

    //Write a query to add a new document to the students collection
    db.students.insertOne({"firstName": "Ron", "lastName": "Weasley", "studentId": "s1019", "houseId": "h1007"})

    //Find the added document to the students collection to prove that it was added
    db.students.find({"lastName": "Weasley"})

    //Write a query to delete the added document from the students collection
    db.students.deleteOne({"firstName": "Ron"})

    //Attempt to find the deleted document from the students collection to prove that it was deleted
    db.students.find({"lastName": "Weasley"})

    //Write a query to search for students by their respective houses
    db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } } ] )

    //Write a query to search for students of house Gryffindor
    db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } }, 
    { $match: {"founder": "Godric Gryffindor"}} ] )

    //Write a query to search for students in the house with the eagle mascot
    db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } }, 
    { $match: {"mascot": "Eagle"}} ] )