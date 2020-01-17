'''
Name: Henry Tsui
Student ID: 20105575
Data: 29th November, 2018
'''


'''
Test for Bike Share Application
'''

import bike

'''
Runs the program, contains data to test the application.
'''
def main():
    data = [['7000', 'Ft.', 'York', '/', 'Capreol', 'Crt.', '43.639832', '-79.395954', '31', '20', '11'],
            ['7001', 'Lower', 'Jarvis', 'St', '/', 'The', 'Esplanade', '43.647992', '-79.370907', '15', '5', '10'],
            ['7002', 'St', 'George', 'St', '/', 'Bloor', 'St', 'W', '43.667333', '-79.399429', '19', '1', '18'],
            ['7003', 'Madison', 'Ave', '/', 'Bloor', 'St', 'W', '43.667158', '-79.402761', '15', '2', '13'],
            ['7004', 'University', 'Ave', '/', 'Elm', 'St', '43.656518', '-79.389099', '11', '0', '11'],
            ['7024', 'Dundonald', 'St' '/', 'Church', 'St', '43.666725', '- 79.381351', '11', '11', '0']]

    # cleanses the data provided
    print(bike.cleanse_data())

    # checks the station whether or not there are bikes available
    print(bike.bike_Availability(data, 7000))

    # allows the user to rent a bike from a specific station
    print(bike.rent_Bike(data, 7000))

    # allows the user to return a bike from a specific station
    print(bike.return_Bike(data, 7000))

    # checks to see if there are stations with available bikes
    print(bike.available_Station(data))

    # checks to see if the docks within a station are full
    print(full_Dock(data))

    # helps directs the user from station to station
    print(bike.show_Directions(data, 7000, 7001))

    # gives information about a specific station to the user
    print(bike.info_Station(data, 7000))


main()
