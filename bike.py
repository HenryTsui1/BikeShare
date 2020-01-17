'''
Name: Henry Tsui
Student ID: 20105575
Data: 16th November, 2018
'''


import urllib.request   # loads a library that is needed for this application.


def readHtml():
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/bikes.txt")
    newList = []  # data is added to this list after running through the for loop
    html = response.readlines()  # reads multiple lines
    for i in html:
        data = i.decode('utf-8').rstrip().split('\t') #splits this line into a list of "tokens", get rids of \t, \n, \r
        newList.append(data)  # adds data to a new list

    newList.pop(0)  # removes the first item of the nested list
    
    return newList


def cleanse_data():
    newList = readHtml()  # tranfers data from readHtml() into variable newList to be called
    newerList = [x for x in newList if x != ['']]  # gets rid of the empty strings

    return newerList


'''
Every time a function has run it's course, this function offers the user a choice whether to return to the menu screen
of the UI or to exit the program.
'''
def menuScreen(data):
    print("")
    print("To return back to MAIN MENU, enter m")
    userinput = input("To exit the application, enter anything.\n""\nEnter: ")

    if userinput == 'm' or userinput == 'M':  # when user inputs m or M it'll bring them back to user_Interface(data)
        user_Interface(data)
    else:
        print("Exiting...")  # otherwise if the user inputs anything else, the program will exit.
        exit()


'''
Provides the user information that they requested for a specific station
'''
def info_Station(data, station):
    print("Information for Station", station)
    print("----------------------------")
    for i in range(len(data)):  #runs through every lists of the list, matching with what the user inputted of index 0
        myList = data[i]
        if myList[0] == str(station):
            print(data[i])  # prints the requested STATION that the user asked for

    menuScreen(data)


'''
To check whether there are bikes or no bikes at a requested station.  If there are available bikes, if grants the user
an option whether or not they would like to rent the bike.
'''
def bike_Availability(data, station):
    print("STATION", station)
    print("------------")
    for i in range(len(data)):
        myList = data[i]
        if myList[0] == str(station):
            if int(myList[-2]) == 0:  # checks the list to see if there are bikes available
                print("There are no available bikes in Station", station)
                print('')
                menuScreen(data)
            else:
                print("There are", myList[-2], "bikes available at Station", station)
                print('')
                userinput = input("If you would like to rent a bike, enter r\nTo return back to MAIN MENU, enter m\n"
                                  "To exit the application, "
                                  "enter anything\n""\nEnter: ")
                if userinput == 'r' or userinput == 'R':  # gives the user the option to rent a bike. Calls rent_Bike()
                    rent_Bike(data, station)
                elif userinput == 'm' or userinput == 'M':
                    user_Interface(data)
                else:
                    print("Exiting...")
                    exit()


'''
User is able to rent a bike from a station if the station has bikes available.  After renting the user will be provided
UPDATED information regarding the bike that they have rented out(Minus 1 for bike availability and add 1 for no. of
docks.  If there are no bikes available, the program will inform the user that they are unable to rent a bike.
'''
def rent_Bike(data, station):
    print("Bike Rental at STATION", station)
    for i in range(len(data)):
        myList = data[i]
        if myList[0] == str(station):
            if int(myList[-2]) > 0:  # sees if the num of bikes exceeds 0. If it does that means there are bikes to rent
                print("You have rented a bike from Station", station)
                print("Updating information to Station", station, "...")
                print("-------------------------------------------------------")
                myList[-2] = str(int(myList[-2]) - 1)   # removes a bike from the list
                myList[-1] = str(int(myList[-1]) + 1)   # frees up a dock from the list
                print("Capacity:", myList[-3], "| Bikes Available:", myList[-2], "| Docks Available:", myList[-1])
                menuScreen(data)
            elif int(myList[-2]) == 0:  # If num of bikes equals 0, means there are no bikes to rent
                print("There has been an error in renting a bike at station", station)
                print("Returning you to the MENU SCREEN...")
                print('')
                user_Interface(data)



'''
User is able to return the bike to a specific station.  After returning the bike the user will be given updated info of
the station that they are returning their bikes to(Add 1 to number of bikes available, minus 1 to number of docks 
available.
'''
def return_Bike(data, station):
    print("Returning bike to STATION", station)
    print("------------------------------")
    for i in range(len(data)):
        myList = data[i]
        if myList[0] == str(station):
            if int(myList[-1]) > 0:  # checks to see whether or not if the docks are full
                print("You have returned a bike to Station", station)  # if not full, you are able to return a bike
                print('')
                print("Updating information to Station", station)
                print("------------------------------------")
                myList[-2] = str(int(myList[-2]) + 1)
                myList[-1] = str(int(myList[-1]) - 1)
                print("Capacity:", myList[-3], "| Bikes Available:", myList[-2], "| Docks Available:", myList[-1])
                menuScreen(data)
            elif int(myList[-1]) == 0:   # if the docks equals to 0, means that the docks are full. Thus user is unable
                                         # to return a bike
                print("There has been an error in returning a bike")
                print("Returning you to the MENU SCREEN...")
                print('')
                user_Interface(data)


'''
Gives the user stations that has bikes available
'''
def available_Station(data):
    data.sort(key=lambda x: int(x[-2]), reverse=True)  # sorts the nested list, from biggest bike value to smallest value
    for row in data:
        print(row)
    return [r for r in data if int(r[-2]) > 0]  # does not return the lists that has 0 bikes


'''
Compares number of bikes with the total capacity of a station.  If both values equal with one another, the station is
therefore seen as being full
'''
def full_Dock(data):
    newList = []
    for i in range(len(data)):  # runs through the lists of list
        myList = data[i]
        if int(myList[-1]) == 0:  # compares index -1 and -3, to see if the station capacity is full
            newList.append(myList)  # adds to a new list named 'newList'
    for j in newList:
        print(j)

    menuScreen(data)

'''
Provides the user directions to travel from their current station to their next station
'''
def show_Directions(data, current_station, next_station):
    print("")
    for i in range(len(data)):
        in_current_station = data[i]
        if in_current_station[0] == str(current_station):
            for j in range(len(data)):
                in_next_station = data[j]
                if in_next_station[0] == str(next_station):
                    current_latitude = float(in_current_station[-5])
                    next_latitude = float(in_next_station[-5])
                    current_longitude = float(in_current_station[-4])
                    next_longitude = float(in_next_station[-4])

                    if current_latitude > next_latitude and current_longitude > next_longitude:
                        print("To go from station", current_station, "to station", next_station, '\n'
                              "Head to the direction of Southwest")
                    elif current_latitude > next_latitude and current_longitude < next_longitude:
                        print("To go from station", current_station, "to station", next_station, '\n'
                              "Head to the direction of Southeast")
                    elif current_latitude < next_latitude and current_longitude > next_longitude:
                        print("To go from station", current_station, "to station", next_station, '\n'
                              "Head to the direction of Northwest")
                    elif current_latitude < next_latitude and current_longitude < next_longitude:
                        print("To go from station", current_station, "to station", next_station, '\n'
                              "Head to the direction of Northwest")
    if current_station == next_station:
        print("You are currently in the same station")

    menuScreen(data)


'''
Serves as the MENU Screen for the Bike Share Application
'''
def user_Interface(data):
    while True:
        print("                       *MENU SCREEN*                         ")
        print("-------------------------------------------------------------")
        print("How can I help you today?")
        print("Enter 1 to search up information of a station.")
        print("Enter 2 to find the directions of a station of your choosing.")
        print("Enter 3 to check bike availability.")
        print("Enter 4 to check all stations.")
        print("Enter 5 to rent out a bike.")

        try:
            userChoice = int(input("Enter 6 to return a bike\nPlease enter a number: "))
        except ValueError:
            print('-------------------------------------------------------------')
            print('                       INVALID INPUT                      ')
            print('-------------------------------------------------------------')
            user_Interface(data)
            continue

        if userChoice == 1:
            while True:
                station = ""
                try:  # if the user enters the appropriate station ID, it continues on try
                    user = int(input("Which station would you like to search for?\nStation: "))
                    print("")
                except ValueError:  # if the user enters something other than a integer, becomes invalid
                    print('')
                    print("INVALID INPUT")
                    print('')
                    continue

                for i in range(len(data)):
                    myList = data[i]
                    if myList[0] == str(user):  # if the station ID matches with the list, returns to the variable above
                        station = user
                        break

                if station != user:
                    print('')
                    print("INVALID STATION ID")  # if station ID doesn't match with the variable, returns as invalid
                    print('')
                else:
                    break

            info_Station(data, station)

        if userChoice == 2:
            while True:  # checks first station ID
                current_station = ""
                try:
                    user = int(input("Which station are you currently at?\nStation: "))
                    print("")
                except ValueError:
                    print('')
                    print("INVALID INPUT")
                    print('')
                    continue

                for i in range(len(data)):
                    myList = data[i]
                    if myList[0] == str(user):
                        current_station = user
                        break

                if current_station != user:
                    print('')
                    print("INVALID STATION ID")
                    print('')
                else:
                    break
            while True:  # checks the next station ID
                next_station = ""
                try:
                    user = int(input('Which station would you like to go?\nStation: '))
                    print('')
                except ValueError:
                    print('')
                    print("INVALID INPUT")
                    print('')
                    continue

                for i in range(len(data)):
                    myList = data[i]
                    if myList[0] == str(user):
                        next_station = user
                        break

                if next_station != user:
                    print('')
                    print("INVALID STATION ID")
                    print('')
                else:
                    break

            show_Directions(data, current_station, next_station)

        if userChoice == 3:
            while True:
                station = ""
                try:
                    user = int(input("Which station would you like to search for?\nStation: "))
                    print("")
                except ValueError:
                    print('')
                    print("INVALID INPUT")
                    print('')
                    continue

                for i in range(len(data)):
                    myList = data[i]
                    if myList[0] == str(user):
                        station = user
                        break

                if station != user:
                    print('')
                    print("INVALID STATION ID")
                    print('')
                else:
                    break
            bike_Availability(data, station)

        if userChoice == 4:
            print("")
            print("List of stations that has bikes available:")
            print("---------------------------")
            available_Station(data)  # calls the function available_Station(data), to check for available stations
            print("")
            print("List of full stations:")
            print("----------------------")
            full_Dock(data)  # calls the function full_Dock(data), to check for full stations

        if userChoice == 5:
            while True:
                station = ""
                try:
                    user = int(input("Which station would you like rent out of?\nStation: "))
                    print("")
                except ValueError:
                    print('')
                    print("INVALID INPUT")
                    print('')
                    continue

                for i in range(len(data)):
                    myList = data[i]
                    if myList[0] == str(user):
                        station = user
                        break

                if station != user:
                    print('')
                    print("INVALID STATION ID")
                    print('')
                else:
                    break
            rent_Bike(data, station)

        if userChoice == 6:
            while True:
                station = ""
                try:
                    user = int(input("Which station would you like to return your bike to?\nStation: "))
                    print("")
                except ValueError:
                    print('')
                    print("INVALID INPUT")
                    print('')
                    continue

                for i in range(len(data)):
                    myList = data[i]
                    if myList[0] == str(user):
                        station = user
                        break

                if station != user:
                    print("INVALID STATION ID")
                else:
                    break
            return_Bike(data, station)




'''
Runs the program, contains data to test the application.
'''
def main():
    data = cleanse_data()
    user_Interface(data)
    #print(cleanse_data())
    #print(available_Station(data))


if __name__ == "__main__":

    main()