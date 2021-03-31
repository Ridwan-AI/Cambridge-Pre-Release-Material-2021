# Task 1
# Start of the day
# Coded by Ridwan Arefin Islam, Need help anywhere? Go to https://caie.rnetworks.cf/
#This is a test2.
print ("\nGood morning\n")

#Initialise structure data for passengers
passenger_left_departure = [480, 480, 480, 480]
passenger_left_return = [480, 480, 480, 480]

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
# print("\033[1;32;40mBright Green\033[0m\n")
wants = "abc"
numoftickets = 0
validcheck = True
purchasesuccess = False
# wants = input("Do you want to purchase some train tickets [Yes/No]?\n")
wantsdeparttime = "100:1000"
while (validcheck == True):
    wants = input("\nDo you want to purchase some train tickets [Yes/No]?\n")
    wants = wants.strip() #Get rid of whitespaces (tabs and spaces) to prevent problems with Yes detection
    if (wants[0] == "Y" or wants[0] == "y"):
            #Wants tickets
            numoftickets = input("How many train tickets do you want to purchase?\n")
            numoftickets = numoftickets.strip() #Get rid of whitespaces (tabs and spaces) to prevent problems with Yes detection
            #Validation that number was entered
            if (numoftickets.isnumeric()):
                numoftickets = int(numoftickets)
            else:
                print ("Please enter a number, properly next time\nSo I'm restarting the questions for you")
                validcheck = True
                continue

            if (numoftickets > 1):
                #Group
                print ("Group ticket selected")
                #Departure time
                wantsdeparttime = input("When do you want to go for departure to the top of the mountain?\n")
                #Validate that tickets are available for departure
                wantsdeparttime = wantsdeparttime.strip()
                if (wantsdeparttime == "09:00" and passenger_left_departure[0]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_departure[0] = passenger_left_departure[0] - numoftickets
                elif (wantsdeparttime == "11:00" and passenger_left_departure[1]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_departure[1] = passenger_left_departure[1] - numoftickets
                elif (wantsdeparttime == "13:00" and passenger_left_departure[2]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_departure[2] = passenger_left_departure[2] - numoftickets
                elif (wantsdeparttime == "15:00" and passenger_left_departure[3]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_departure[3] = passenger_left_departure[3] - numoftickets
                else:
                    print ("\033[1;31;40mDeparture ticket purchase failed, either due to one of the reasons below:\n•Not enough tickets available for that time slot\n•You entered such a time slot that does not exist\033[0m")
                #Return time
                wantsreturntime = input("When do you want to return from the top of the mountain?\n")
                wantsreturntime = wantsreturntime.strip()
                #Validate that tickets are available for return
                if (wantsreturntime == "10:00" and passenger_left_return[0]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_return[0] = passenger_left_return[0] - numoftickets
                elif (wantsreturntime == "12:00" and passenger_left_return[1]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_return[1] = passenger_left_return[1] - numoftickets
                elif (wantsreturntime == "14:00" and passenger_left_return[2]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_return[2] = passenger_left_return[2] - numoftickets
                elif (wantsreturntime == "16:00" and passenger_left_return[3]>=numoftickets):
                    print ("\033[1;32Departure tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_return[3] = passenger_left_return[3] - numoftickets
                else:
                    print ("\033[1;31;40mDeparture ticket purchase failed, either due to one of the reasons below:\n•Not enough tickets available for that time slot\n•You entered such a time slot that does not exist\033[0m")
                
            elif (numoftickets == 1):
                #Single
                print ("Single ticket selected.")
                wantsdeparttime = input("When do you want to go for departure to the top of the mountain?\n")
                wantsdeparttime = wantsdeparttime.strip()
                #Validate that tickets are available for departure
                if (wantsdeparttime == "09:00" and passenger_left_departure[0]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_departure[0] = passenger_left_departure[0] - numoftickets
                elif (wantsdeparttime == "11:00" and passenger_left_departure[1]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_departure[1] = passenger_left_departure[1] - numoftickets
                elif (wantsdeparttime == "13:00" and passenger_left_departure[2]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_departure[2] = passenger_left_departure[2] - numoftickets
                elif (wantsdeparttime == "15:00" and passenger_left_departure[3]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_departure[3] = passenger_left_departure[3] - numoftickets
                else:
                    print ("\033[1;31;40mDeparture ticket purchase failed, either due to one of the reasons below:\n•Not enough tickets available for that time slot\n•You entered such a time slot that does not exist\033[0m")
                #Return time
                wantsreturntime = input("When do you want to return from the top of the mountain?\n")
                wantsreturntime = wantsreturntime.strip()
                #Validate that tickets are available for return
                if (wantsreturntime == "10:00" and passenger_left_return[0]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_return[0] = passenger_left_return[0] - numoftickets
                elif (wantsreturntime == "12:00" and passenger_left_return[1]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_return[1] = passenger_left_return[1] - numoftickets
                elif (wantsreturntime == "14:00" and passenger_left_return[2]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_return[2] = passenger_left_return[2] - numoftickets
                elif (wantsreturntime == "16:00" and passenger_left_return[3]>=numoftickets):
                    print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                    purchasesuccess = True
                    passenger_left_return[3] = passenger_left_return[3] - numoftickets
                else:
                    print ("\033[1;31;40mDeparture ticket purchase failed, either due to one of the reasons below:\n•Not enough tickets available for that time slot\n•You entered such a time slot that does not exist\033[0m")
            else:
                #Validation failed
                print("Please enter properly.")

    elif (wants[0] == "N" or wants[0] == "n"): 
            #Doesn't want tickets
            print ("You selected no so not giving you tickets.")
            validcheck = False
    else:
            #We don't know what he wants because of wrong input
            print ("Please enter again properly.")
            validcheck = True
    if (purchasesuccess == True):
        purchasesuccess = False
        print ("\nTrain times and remaining tickets along with price are shown below:")
        print ("Departure to top of mountain                                                         Return from top of mountain")
        print ("Time: 09:00  Tickets remaining: " + str(passenger_left_departure[0]) + "  Money collected: " + str(totalmoney_departure[0]) + "  Price: $25/ticket" + "           Time: 10:00  Tickets remaining: " + str(passenger_left_return[0]) + "  Money collected: " + str(totalmoney_return[0]) + "  Price: $25/ticket")
        print ("Time: 11:00  Tickets remaining: " + str(passenger_left_departure[1]) + "  Money collected: " + str(totalmoney_departure[1]) + "  Price: $25/ticket" + "           Time: 12:00  Tickets remaining: " + str(passenger_left_return[1]) + "  Money collected: " + str(totalmoney_return[1]) + "  Price: $25/ticket")
        print ("Time: 13:00  Tickets remaining: " + str(passenger_left_departure[2]) + "  Money collected: " + str(totalmoney_departure[2]) + "  Price: $25/ticket" + "           Time: 14:00  Tickets remaining: " + str(passenger_left_return[2]) + "  Money collected: " + str(totalmoney_return[2]) + "  Price: $25/ticket")
        print ("Time: 15:00  Tickets remaining: " + str(passenger_left_departure[3]) + "  Money collected: " + str(totalmoney_departure[3]) + "  Price: $25/ticket" + "           Time: 16:00  Tickets remaining: " + str(passenger_left_return[3]) + "  Money collected: " + str(totalmoney_return[3]) + "  Price: $25/ticket")




#Just a newline to make output look nicer
print ("")
