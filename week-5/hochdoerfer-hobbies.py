#----------------------------------------------------------
# Title: hochdoerfer_hobbies.py
# Author: Kyle Hochdoerfer
# Date: 09/04/23
# Description: Code for iterating through lists
#----------------------------------------------------------

#Create a Python list with five hobbies
hobby_list = ["tennis", "jogging", "video games", "writing", "reading"]

#Create a list containing the days of the week
day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Print all hobbies in the list to the console
for x in hobby_list:
    print(x)

#For each day in the list
for d in day_list:
    #Create a message variable for printing the status of a day
    day_message = d
    #If the day is saturday or sunday
    if d == 'Sunday' or d == 'Saturday':
        #Concatenate a message stating that the current day is for enjoying hobbies
        day_message += " is a day for enjoying hobbies"
    else:
        #Otherwise, concatenate a message stating that the current day is a work day
        day_message += " is a work day"
    #Print the day_message
    print(day_message)