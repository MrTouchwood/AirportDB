# -*- coding: utf-8 -*-

import mysql.connector


def connect_database():
    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )

    return mydb


def printDirections():
    directions = """
        Enter one of the following options:

        search flights          insert flight           update flight           delete flights
        search company          insert company          update company          delete company
        search controller       insert controller       update controller       delete controller
        search engineer         insert engineer         update engineer         delete engineer
        search freighter        insert freighter        update freighter        delete freighter
        search plane            insert plane            update plane            delete plane
        search load             insert load                                     delete load
        search service          insert service                                  delete service

        check gates <minutes>
        check airstrip <minutes>

        exit

        """

    print(directions)


def chooseFunction(mydb):
    x = input("[AirportDB ~]$ ")
    while (x != "exit"):

        if x == "search flights":
            searchFlights(mydb)

        elif x == "search company":
            searchCompany(mydb)

        elif x == "search controller":
            searchController(mydb)

        elif x == "search engineer":
            searchEngineer(mydb)

        elif x == "search freighter":
            searchFreighter(mydb)

        elif x == "search load":
            searchLoad(mydb)

        elif x == "search plane":
            searchPlane(mydb)

        elif x == "search service":
            searchService(mydb)

        elif x == "delete flights":
            deleteFlights(mydb)

        elif x == "delete company":
            deleteCompany(mydb)

        elif x == "delete controller":
            deleteController(mydb)

        elif x == "delete engineer":
            deleteEngineer(mydb)

        elif x == "delete freighter":
            deleteFreighter(mydb)

        elif x == "delete load":
            deleteLoad(mydb)

        elif x == "delete plane":
            deletePlane(mydb)

        elif x == "delete service":
            deleteService(mydb)

        elif x == "insert flight":
            insertFlight(mydb)

        elif x == "insert company":
            insertCompany(mydb)

        elif x == "insert controller":
            insertController(mydb)

        elif x == "insert engineer":
            insertEngineer(mydb)

        elif x == "insert frighter":
            insertFreighter(mydb)

        elif x == "insert load":
            insertLoad(mydb)

        elif x == "insert plane":
            insertPlane(mydb)

        elif x == "insert service":
            insertService(mydb)

        elif x == "update flight":
            updateFlight(mydb)

        elif x == "update company":
            updateCompany(mydb)

        elif x == "update controller":
            updateController(mydb)

        elif x == "update engineer":
            updateEngineer(mydb)

        elif x == "update freighter":
            updateFreighter(mydb)

        elif x == "update plane":
            updatePlane(mydb)

        elif x == "check gates":
            checkGates(mydb, 30)

        elif x == "check airstrip":
            checkAirstrip(mydb, 15)

        else:
            analysis = x.split()
            if len(analysis) == 3:
                if analysis[0] == 'check':
                    check_minutes = 30
                    try:
                        check_minutes = int(analysis[2])
                    except:
                        print("Invalid Input")

                    if analysis[1] == 'gates':
                        checkGates(mydb, check_minutes)
                    if analysis[1] == 'airstrip':
                        checkAirstrip(mydb, check_minutes)

        x = input("[AirportDB ~]$ ")


def ask_data(data):
    message = "Enter " + data
    print(message)
    x = input()
    return x


def searchFlights(mydb):
    directions = """
    print all
    flight id,
    plane id,
    departure,
    destination,
    departure time,
    arrival time,
    real departure time,
    controller,
    status,
    gate id,
    airstrip id,
    parking spot id,
    parking start,
    parking end
    search dates
    """

    keys = ["flight id: ", "plane id: ", "departure: ", "destination: ", "departure time: ", "arrival time: ",
            "real departure time: ", "controller: ", "status: ", "gate id: ", "airstrip id: ", "parking spot id: ",
            "parking start date: ", "parking end date: "]

    keys_dates = ["flight id: ", "plane id: ", "departure: ", "destination: ", "departure time: ", "arrival time: ",
                  "gate id: "]

    message = "Enter one of the above options to select flights:"

    print(directions)
    option = input("Enter one of the above options to select flights: ")

    if option == "departure time" or option == "arrival time" or option == "parking start" or option == "parking end":
        print("Enter datetime data as follows: 2020-03-23 18:00:00")

    if option == "search dates":
        print("Enter date with this format: 2021-03-20")
        start_date = input("Enter start date to search:")
        last_date = input("Enter last date to search:")
        start_datetime = start_date + " 00:00:00"
        last_datetime = last_date + " 23:59:59"
    if option == "print all":

        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM Flight;")

            i = 1
            for row in mycursor:
                print()
                print("Flight " + str(i) + " information:")
                print("------------------")
                i = i + 1
                for counter in range(len(row)):
                    result = keys[counter] + str(row[counter])
                    print(result)
                print()

        except:
            print("Invalid data entered. Try again.")
        return

    else:
        message1 = "Enter " + option + " to search for flights:"
        print(message1)
        data = input()

    queries = {
        "flight id": "SELECT * FROM Flight WHERE FlightID = %s;",
        "plane id": "SELECT * FROM Flight WHERE PlaneID = %s;",
        "departure": "SELECT * FROM Flight WHERE Departure = %s;",
        "destination": "SELECT * FROM Flight WHERE Destination = %s;",
        "departure time": "SELECT * FROM Flight WHERE DepartTime = %s;",
        "arrival time": "SELECT * FROM Flight WHERE ArrivalTime = %s;",
        "real departure time": "SELECT * FROM Flight WHERE RealDepartTime = %s;",
        "controller": "SELECT * FROM Flight WHERE Controller = %s;",
        "status": "SELECT * FROM Flight WHERE Status = %s;",
        "gate id": "SELECT * FROM Flight WHERE GateID = %s;",
        "airstrip id": "SELECT * FROM Flight WHERE AirstripID = %s;",
        "parking spot id": "SELECT * FROM Flight WHERE ParkingSpotID = %s;",
        "parking start": "SELECT * FROM Flight WHERE ParkingStart = %s;",
        "parking end": "SELECT * FROM Flight WHERE ParkingEnd = %s;",
        "search dates": "SELECT FlightID,PlaneID,Departure,Destination,DepartTime,ArrivalTime,GateID FROM flight WHERE ((DepartTime BETWEEN %s AND %s AND Departure='UPA') OR (ArrivalTime BETWEEN %s AND %s AND Destination='UPA'));"
    }

    if option == "search dates":

        mytuple = (start_datetime, last_datetime, start_datetime, last_datetime)

        try:
            mycursor = mydb.cursor()
            mycursor.execute(queries[option], mytuple)

            i = 1
            for row in mycursor:
                print()
                print("Flight " + str(i) + " information:")
                print("------------------")
                i = i + 1
                for counter in range(len(row)):
                    result = keys_dates[counter] + str(row[counter])
                    print(result)
                print()

        except:
            print("Invalid data entered. Try again.")


    else:
        try:
            mycursor = mydb.cursor()
            mycursor.execute(queries[option], tuple([data]))

            i = 1
            for row in mycursor:
                print()
                print("Flight " + str(i) + " information:")
                print("------------------")
                i = i + 1
                for counter in range(len(row)):
                    result = keys[counter] + str(row[counter])
                    print(result)
                print()

        except:
            print("Invalid data entered. Try again.")


def searchCompany(mydb):
    directions = """
    name,
    phone    
    """

    print(directions)
    option = input("Enter one of the above options to select a comapny: ")

    message1 = "Enter " + option + " to search for a company:"
    print(message1)
    data = input()

    queries = {
        "name": "SELECT * FROM Company WHERE Name = %s;",
        "phone": "SELECT * FROM Company WHERE Phone = %s;"
    }

    keys = ["name: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print()
            print("Company " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def searchController(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    option = input("Enter one of the above options to select a controller: ")

    message1 = "Enter " + option + " to search for a controller:"
    print(message1)
    data = input()

    queries = {
        "id": "SELECT * FROM Controller WHERE ID = %s;",
        "name": "SELECT * FROM Controller WHERE Name = %s;",
        "surname": "SELECT * FROM Controller WHERE Surname = %s;",
        "phone": "SELECT * FROM Controller WHERE Phone = %s;"
    }

    keys = ["id: ", "name: ", "surname: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print()
            print("Controller " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def searchEngineer(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    option = input("Enter one of the above options to select an engineer: ")

    message1 = "Enter " + option + " to search for an engineer:"
    print(message1)
    data = input()

    queries = {
        "id": "SELECT * FROM Engineer WHERE EngineerID = %s;",
        "name": "SELECT * FROM Engineer WHERE Name = %s;",
        "surname": "SELECT * FROM Engineer WHERE Surname = %s;",
        "phone": "SELECT * FROM Engineer WHERE Phone = %s;"
    }

    keys = ["id: ", "name: ", "surname: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print()
            print("Engineer " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def searchFreighter(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    option = input("Enter one of the above options to select a freighter: ")

    message1 = "Enter " + option + " to search for a freighter:"
    print(message1)
    data = input()

    queries = {
        "id": "SELECT * FROM Freighter WHERE FreighterID = %s;",
        "name": "SELECT * FROM Freighter WHERE Name = %s;",
        "surname": "SELECT * FROM Freighter WHERE Surname = %s;",
        "phone": "SELECT * FROM Freighter WHERE Phone = %s;"
    }

    keys = ["id: ", "name: ", "surname: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print()
            print("Freighter " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def searchLoad(mydb):
    directions = """
    flight id,
    freighter id   
    """

    print(directions)
    option = input("Enter one of the above options to select a load: ")

    message1 = "Enter " + option + " to search for a load:"
    print(message1)
    data = input()

    queries = {
        "flight id": "SELECT * FROM Loads WHERE FlightID = %s;",
        "freighter id": "SELECT * FROM Loads WHERE FreighterID = %s;"
    }

    keys = ["id: ", "name: ", "surname: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print()
            print("Load " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def searchPlane(mydb):
    directions = """
    id,
    owner,
    maker,
    model   
    """

    print(directions)
    option = input("Enter one of the above options to select a plane: ")

    message1 = "Enter " + option + " to search for a plane:"
    print(message1)
    data = input()

    queries = {
        "id": "SELECT * FROM Plane WHERE ID = %s;",
        "owner": "SELECT * FROM Plane WHERE Owner = %s;",
        "maker": "SELECT * FROM Plane WHERE Maker = %s;",
        "model": "SELECT * FROM Plane WHERE Model = %s;"
    }

    keys = ["id: ", "owner: ", "maker: ", "model: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print()
            print("Plane " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def searchService(mydb):
    directions = """
    flight id,
    engineer id 
    """

    print(directions)
    option = input("Enter one of the above options to select a service: ")

    message1 = "Enter " + option + " to search for a service:"
    print(message1)
    data = input()

    queries = {
        "flight id": "SELECT * FROM Services WHERE FlightID = %s;",
        "engineer": "SELECT * FROM Services WHERE EngineerID = %s;"
    }

    keys = ["flight id: ", "engineer: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print()
            print("Service " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def deleteFlights(mydb):
    directions = """
    flight id,
    plane id,
    departure,
    destination,
    departure time,
    arrival time,
    controller,
    status,
    gate id,
    airstrip id,
    parking spot id,
    parking start,
    parking end    
    """

    print(directions)
    option = input("Enter one of the above options to delete flights: ")

    if option == "deaprture time" or option == "arrival time" or option == "parking start" or option == "parking end":
        print("Enter datetime data as follows: 2020-03-23 18:00:00")

    message1 = "Enter " + option + " to delete flights:"
    print(message1)
    data = input()

    queries = {
        "flight id": "DELETE FROM Flight WHERE FlightID = %s;",
        "plane id": "DELETE FROM Flight WHERE PlaneID = %s;",
        "departure": "DELETE FROM Flight WHERE Departure = %s;",
        "destination": "DELETE FROM Flight WHERE Destination = %s;",
        "departure time": "DELETE FROM Flight WHERE DepartTime = %s;",
        "arrival time": "DELETE FROM Flight WHERE ArrivalTime = %s;",
        "controller": "DELETE FROM Flight WHERE Controller = %s;",
        "status": "DELETE FROM Flight WHERE Status = %s;",
        "gate id": "DELETE FROM Flight WHERE GateID = %s;",
        "airstrip id": "DELETE FROM Flight WHERE AirstripID = %s;",
        "parking spot id": "DELETE FROM Flight WHERE ParkingSpotID = %s;",
        "parking start": "DELETE FROM Flight WHERE ParkingStart = %s;",
        "parking end": "DELETE FROM Flight WHERE ParkingEnd = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteCompany(mydb):
    directions = """
    name,
    phone    
    """

    print(directions)
    option = input("Enter one of the above options to delete a comapny: ")

    message1 = "Enter " + option + " to delete a company:"
    print(message1)
    data = input()

    queries = {
        "name": "DELETE FROM Company WHERE Name = %s;",
        "phone": "DELETE FROM Company WHERE Phone = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteController(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    option = input("Enter one of the above options to delete a controller: ")

    message1 = "Enter " + option + " to delete a controller:"
    print(message1)
    data = input()

    queries = {
        "id": "DELETE FROM Controller WHERE ID = %s;",
        "name": "DELETE FROM Controller WHERE Name = %s;",
        "surname": "DELETE FROM Controller WHERE Surname = %s;",
        "phone": "DELETE FROM Controller WHERE Phone = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteEngineer(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    option = input("Enter one of the above options to delete an engineer: ")

    message1 = "Enter " + option + " to delete an engineer:"
    print(message1)
    data = input()

    queries = {
        "id": "DELETE FROM Engineer WHERE EngineerID = %s;",
        "name": "DELETE FROM Engineer WHERE Name = %s;",
        "surname": "DELETE FROM Engineer WHERE Surname = %s;",
        "phone": "DELETE FROM Engineer WHERE Phone = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteFreighter(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    option = input("Enter one of the above options to delete a freighter: ")

    message1 = "Enter " + option + " to delete a freighter:"
    print(message1)
    data = input()

    queries = {
        "id": "DELETE FROM Freighter WHERE FreighterID = %s;",
        "name": "DELETE FROM Freighter WHERE Name = %s;",
        "surname": "DELETE FROM Freighter WHERE Surname = %s;",
        "phone": "DELETE FROM Freighter WHERE Phone = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteLoad(mydb):
    directions = """
    flight id,
    freighter id    
    """

    print(directions)
    option = input("Enter one of the above options to delete a load: ")

    message1 = "Enter " + option + " to delete a load:"
    print(message1)
    data = input()

    queries = {
        "flight id": "DELETE FROM Loads WHERE FlightID = %s;",
        "freighter id": "DELETE FROM Loads WHERE FreighterID = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deletePlane(mydb):
    directions = """
    id,
    owner,
    maker,
    model    
    """

    print(directions)
    option = input("Enter one of the above options to delete a plane: ")

    message1 = "Enter " + option + " to delete a plane:"
    print(message1)
    data = input()

    queries = {
        "id": "DELETE FROM Plane WHERE ID = %s;",
        "owner": "DELETE FROM Plane WHERE Owner = %s;",
        "maker": "DELETE FROM Plane WHERE Maker = %s;",
        "model": "DELETE FROM Plane WHERE Model = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteService(mydb):
    directions = """
    flight id,
    engineer id    
    """

    print(directions)
    option = input("Enter one of the above options to delete a service: ")

    message1 = "Enter " + option + " to delete a service:"
    print(message1)
    data = input()

    queries = {
        "flight id": "DELETE FROM Services WHERE FlightID = %s;",
        "engineer id": "DELETE FROM Services WHERE EngineerID = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def insertFlight(mydb):
    mycursor = mydb.cursor()

    flight = {
        "flight_id:": "",
        "plane_id:": "",
        "departure:": "",
        "destination:": "",
        "departure time:": "",
        "arrival time:": "",
        "real departure time:": "",
        "controller:": "",
        "status:": "",
        "gate_id:": "",
        "airstrip_id:": "",
        "parkingspot_id:": "",
        "parking start date:": "",
        "parking end date:": ""
    }

    for key in flight:
        flight[key] = ask_data(key)
        print(flight[key])

    try:
        mycursor.execute(
            "INSERT INTO Flight (FlightID,PlaneID,Departure,Destination,DepartTime,ArrivalTime,RealDepartTime,Controller,Status,GateID,AirstripID,ParkingSpotID,ParkingStart,ParkingEnd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (flight['flight_id:'], flight['plane_id:'], flight['departure:'], flight['destination:'],
             flight['departure time:'], flight['arrival time:'], flight['real departure time:'], flight['controller:'],
             flight['status:'], flight['gate_id:'], flight['airstrip_id:'], flight['parkingspot_id:'],
             flight['parking start date:'], flight['parking end date:']))
    except:
        print("You entered invalid data. Try again.")

    mydb.commit()
    print("Data inserted successfully.")


def insertCompany(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "company name:": "",
        "company phone:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO Company (Name,Phone) VALUES (%s,%s)",
                         (mydict['company name:'], mydict['company phone:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertController(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "controller id:": "",
        "controller name:": "",
        "controller surname:": "",
        "controller phone:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO Controller (ID,Name,Surname,Phone) VALUES (%s,%s,%s,%s)", (
            mydict['controller id:'], mydict['controller name:'], mydict['controller surname:'],
            mydict['controller phone:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertEngineer(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "engineer id:": "",
        "engineer name:": "",
        "engineer surname:": "",
        "engineer phone:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO Engineer (EngineerID,Name,Surname,Phone) VALUES (%s,%s,%s,%s)", (
            mydict['engineer id:'], mydict['engineer name:'], mydict['engineer surname:'], mydict['engineer phone:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertFreighter(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "freighter id:": "",
        "freighter name:": "",
        "freighter surname:": "",
        "freighter phone:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO Freighter (FreighterID,Name,Surname,Phone) VALUES (%s,%s,%s,%s)", (
            mydict['freighter id:'], mydict['freighter name:'], mydict['freighter surname:'],
            mydict['freighter phone:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertLoad(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "flight id:": "",
        "freighter id:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO Loads (FlightID,FreighterID) VALUES (%s,%s)",
                         (mydict['flight id:'], mydict['freighter id:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertPlane(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "plane id:": "",
        "plane owner:": "",
        "plane maker:": "",
        "plane model:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO Plane (ID,Owner,Maker,Model) VALUES (%s,%s,%s,%s)",
                         (mydict['plane id:'], mydict['plane owner:'], mydict['plane maker:'], mydict['plane model:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertService(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "flight id:": "",
        "engineer id:": ""
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO Services (FlightID,EngineerID) VALUES (%s,%s)",
                         (mydict['flight id:'], mydict['engineer id:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def updateFlight(mydb):
    print("Enter flight ID:")
    flight_id = input()

    directions = """
    flight_id,
    plane_id,
    departure,
    destination,
    departure time,
    arrival time,
    real departure time,
    controller,
    status,
    gate_id,
    airstrip_id,
    parkingspot_id,
    parking start date,
    parking end date    
    """

    print(directions)
    choice = input("Enter one of the above fields to update it: ")

    flight = {
        "flight_id": "FlightID",
        "plane_id": "PlaneID",
        "departure": "Departure",
        "destination": "Destination",
        "departure time": "DepartTime",
        "arrival time": "ArrivalTime",
        "real departure time": "RealDepartTime",
        "controller": "Controller",
        "status": "Status",
        "gate_id": "GateID",
        "airstrip_id": "AirstripID",
        "parkingspot_id": "ParkingSpotID",
        "parking start date": "ParkingStart",
        "parking end date": "ParkingEnd"
    }

    queries = {
        "flight_id": "UPDATE Flight SET FlightID = %s WHERE FlightID = %s;",
        "plane_id": "UPDATE Flight SET PlaneID = %s WHERE FlightID = %s;",
        "departure": "UPDATE Flight SET Departure = %s WHERE FlightID = %s;",
        "destination": "UPDATE Flight SET Destination = %s WHERE FlightID = %s;",
        "departure time": "UPDATE Flight SET DepartTime = %s WHERE FlightID = %s;",
        "arrival time": "UPDATE Flight SET ArrivalTime = %s WHERE FlightID = %s;",
        "real departure time": "UPDATE Flight SET RealDepartTime = %s WHERE FlightID = %s;",
        "controller": "UPDATE Flight SET Controller = %s WHERE FlightID = %s;",
        "status": "UPDATE Flight SET Status = %s WHERE FlightID = %s;",
        "gate_id": "UPDATE Flight SET GateID = %s WHERE FlightID = %s;",
        "airstrip_id": "UPDATE Flight SET AirstripID = %s WHERE FlightID = %s;",
        "parkingspot_id": "UPDATE Flight SET ParkingSpotID = %s WHERE FlightID = %s;",
        "parking start date": "UPDATE Flight SET ParkingStart = %s WHERE FlightID = %s;",
        "parking end date": "UPDATE Flight SET ParkingEnd = %s WHERE FlightID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in flight:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, flight_id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updateCompany(mydb):
    print("Enter companies' name:")
    company_name = input()

    directions = """
    name,
    phone    
    """

    print(directions)
    choice = input("Enter one of the above fields to update it: ")

    company = {
        "name": "Name",
        "phone": "Phone"
    }

    queries = {
        "name": "UPDATE Company SET Name = %s WHERE Name = %s;",
        "phone": "UPDATE Company SET Phone = %s WHERE Name = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in company:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, company_name))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updateController(mydb):
    print("Enter controller's id:")
    controller_id = input()

    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    choice = input("Enter one of the above fields to update it: ")

    controller = {
        "id": "ID",
        "name": "Name",
        "surname": "Surname",
        "phone": "Phone"
    }

    queries = {
        "id": "UPDATE Controller SET ID = %s WHERE ID = %s;",
        "name": "UPDATE Controller SET Name = %s WHERE ID = %s;",
        "surname": "UPDATE Controller SET Surname = %s WHERE ID = %s;",
        "phone": "UPDATE Controller SET Phone = %s WHERE ID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in controller:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, controller_id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updateEngineer(mydb):
    print("Enter engineer's id:")
    engineer_id = input()

    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    choice = input("Enter one of the above fields to update it: ")

    engineer = {
        "id": "EngineerID",
        "name": "Name",
        "surname": "Surname",
        "phone": "Phone"
    }

    queries = {
        "id": "UPDATE Engineer SET EngineerID = %s WHERE EngineerID = %s;",
        "name": "UPDATE Engineer SET Name = %s WHERE EngineerID = %s;",
        "surname": "UPDATE Engineer SET Surname = %s WHERE EngineerID = %s;",
        "phone": "UPDATE Engineer SET Phone = %s WHERE EngineerID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in engineer:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, engineer_id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updateFreighter(mydb):
    print("Enter freighter's id:")
    id = input()

    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    choice = input("Enter one of the above fields to update it: ")

    freighter = {
        "id": "FreighterID",
        "name": "Name",
        "surname": "Surname",
        "phone": "Phone"
    }

    queries = {
        "id": "UPDATE Freighter SET FreighterID = %s WHERE FreighterID = %s;",
        "name": "UPDATE Freighter SET Name = %s WHERE FreighterID = %s;",
        "surname": "UPDATE Freighter SET Surname = %s WHERE FreighterID = %s;",
        "phone": "UPDATE Freighter SET Phone = %s WHERE FreighterID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in freighter:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updatePlane(mydb):
    print("Enter plane's id:")
    id = input()

    directions = """
    id,
    maker,
    model    
    """

    print(directions)
    choice = input("Enter one of the above fields to update it: ")

    plane = {
        "id": "ID",
        "maker": "Maker",
        "model": "Model"
    }

    queries = {
        "id": "UPDATE Plane SET ID = %s WHERE ID = %s;",
        "Maker": "UPDATE Plane SET Maker = %s WHERE ID = %s;",
        "Model": "UPDATE Plane SET Model = %s WHERE ID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in plane:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def checkGates(mydb, check_minutes):
    check_minutes = str(check_minutes)
    query = '''SELECT A.FlightID, B.FlightID,A.destination,A.GateID,abs(TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime)) AS minutes FROM Flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.GateID=B.GateID) WHERE ((A.Destination='UPA') AND (B.Destination='UPA') AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime))<%s) )
    UNION SELECT A.FlightID, B.FlightID,A.departure,A.GateID,abs(TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime)) AS minutes FROM Flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.GateID=B.GateID) WHERE ((A.Departure='UPA') AND (B.Departure='UPA') AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime))<%s) )
    UNION SELECT A.FlightID, B.FlightID,A.departure,A.GateID,abs(TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime)) AS minutes FROM Flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.GateID=B.GateID) WHERE ((A.Departure='UPA') AND (B.Destination='UPA') AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime))<%s) )
    UNION SELECT A.FlightID, B.FlightID,A.destination,A.GateID,abs(TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime)) AS minutes FROM Flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.GateID=B.GateID) WHERE ((A.Destination='UPA') AND (B.Departure='UPA') AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime))<%s) );'''
    mytuple = (check_minutes, check_minutes, check_minutes, check_minutes, check_minutes, check_minutes, check_minutes,
               check_minutes)

    keys = ["flight 1: ", "flight 2: ", "airport: ", "gate: ", "time difference: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(query, mytuple)

        i = 1
        for row in mycursor:
            print()
            print("Collision: "+str(i))
            print("------------------")
            i += 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def checkAirstrip(mydb, check_minutes):
    check_minutes = str(check_minutes)
    query = '''SELECT A.FlightID, B.FlightID,A.destination,A.AirstripID,abs(TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime)) AS minutes FROM Flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.AirstripID=B.AirstripID) WHERE ((A.Destination='UPA') AND (B.Destination='UPA') AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime))<%s) )
        UNION SELECT A.FlightID, B.FlightID,A.departure,A.AirstripID,abs(TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime)) AS minutes FROM Flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.AirstripID=B.AirstripID) WHERE ((A.Departure='UPA') AND (B.Departure='UPA') AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime))<%s) )
        UNION SELECT A.FlightID, B.FlightID,A.departure,A.AirstripID,abs(TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime)) AS minutes FROM Flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.AirstripID=B.AirstripID) WHERE ((A.Departure='UPA') AND (B.Destination='UPA') AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime))<%s) )
        UNION SELECT A.FlightID, B.FlightID,A.destination,A.AirstripID,abs(TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime)) AS minutes FROM Flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.AirstripID=B.AirstripID) WHERE ((A.Destination='UPA') AND (B.Departure='UPA') AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime))<%s) );'''
    mytuple = (check_minutes, check_minutes, check_minutes, check_minutes, check_minutes, check_minutes, check_minutes,
               check_minutes)

    keys = ["flight 1: ", "flight 2: ", "airport: ", "airstrip: ", "time difference: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(query, mytuple)

        i = 1
        for row in mycursor:
            print()
            print("Collision: "+str(i))
            print("------------------")
            i += 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print()

    except:
        print("Invalid data entered. Try again.")


def main():
    mydb = connect_database()
    printDirections()
    chooseFunction(mydb)

    exit(1)


main()








