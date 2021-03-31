# Task 1
# Start of the day
# Coded by Ridwan Arefin Islam, Need help anywhere? Go to https://caie.rnetworks.cf/
#This is a test2.
print ("\nGood morning\n")

#Initialise structure data for passengers
passenger_left_departure = (480, 480, 480, 480)
passenger_left_return = (480, 480, 480, 480)

#Initialise structure data for money collected
totalmoney_departure = (0, 0, 0, 0)
totalmoney_return = (0, 0, 0, 0)

#Screen display code
print ("Train times and remaining tickets along with price are shown below:")
print ("Departure to top of mountain                                                         Return from top of mountain")
print ("Time: 09:00  Tickets remaining: " + str(passenger_left_departure[0]) + "  Money collected: " + str(totalmoney_departure[0]) + "  Price: $25/ticket" + "           Time: 10:00  Tickets remaining: " + str(passenger_left_return[0]) + "  Money collected: " + str(totalmoney_return[0]) + "  Price: $25/ticket")
print ("Time: 11:00  Tickets remaining: " + str(passenger_left_departure[1]) + "  Money collected: " + str(totalmoney_departure[1]) + "  Price: $25/ticket" + "           Time: 12:00  Tickets remaining: " + str(passenger_left_return[1]) + "  Money collected: " + str(totalmoney_return[1]) + "  Price: $25/ticket")
print ("Time: 13:00  Tickets remaining: " + str(passenger_left_departure[2]) + "  Money collected: " + str(totalmoney_departure[2]) + "  Price: $25/ticket" + "           Time: 14:00  Tickets remaining: " + str(passenger_left_return[2]) + "  Money collected: " + str(totalmoney_return[2]) + "  Price: $25/ticket")
print ("Time: 15:00  Tickets remaining: " + str(passenger_left_departure[3]) + "  Money collected: " + str(totalmoney_departure[3]) + "  Price: $25/ticket" + "           Time: 16:00  Tickets remaining: " + str(passenger_left_return[3]) + "  Money collected: " + str(totalmoney_return[3]) + "  Price: $25/ticket")

print("")
# Task 2

# Purchasing tickets

wants = "abc"
numoftickets = 0
validcheck = True
# wants = input("Do you want to purchase some train tickets [Yes/No]?\n")

while True:
    wants = input("Do you want to purchase some train tickets [Yes/No]?\n")
    if (wants[0] == "Y" or wants[0] == "y"):
            #Wants tickets
            numoftickets = input("How many train tickets do you want to purchase?\n")
            
            #Validation that number was entered
            if (numoftickets.isnumeric()):
                numoftickets = int(numoftickets)
            else:
                print ("Please enter a number, properly next time\nSo I'm restarting the questions for you")
                validcheck = True
                continue

            if (numoftickets > 1):
                #Group
                print ("Alright giving you a group ticket.")
                
            elif (numoftickets == 1):
                #Single
                print ("Alright giving you a single ticket.")
            else:
                #Validation failed
                print("Please enter properly.")

    elif (wants[0] == "N" or wants[0] == "n"): 
            #Doesn't want tickets
            print ("You selected no so not giving you tickets.")
    else:
            #We don't know what he wants because of wrong input
            print ("Please enter again properly.")
            validcheck = False
    if (validcheck == True):
        break
#Just a newline to make output look nicer
print ("")