################################################# Task 1 #################################################
############################################# Start of the day ###########################################
# Coded by Ridwan Arefin Islam, Need help anywhere? Go to https://caiefinder.com/  Email me at ridwan@caiefinder.com

print ("\nGood morning\n")

#Initialise structure data for passengers
passenger_left_departure = [480, 480, 480, 480]
passenger_left_return = [480, 480, 480, 480]

#Initialise structure data for money collected
totalmoney_departure = [0, 0, 0, 0]
totalmoney_return = [0, 0, 0, 0]

#Screen display code
print ("\033[1;34;40mTrain times and remaining tickets along with price are shown below:")
print ("Departure to top of mountain                                                         Return from top of mountain")
print ("Time: 09:00  Tickets remaining: " + str(passenger_left_departure[0]) + "  Money collected: " + str(totalmoney_departure[0]) + "  Price: $25/ticket" + "           Time: 10:00  Tickets remaining: " + str(passenger_left_return[0]) + "  Money collected: " + str(totalmoney_return[0]) + "  Price: $25/ticket")
print ("Time: 11:00  Tickets remaining: " + str(passenger_left_departure[1]) + "  Money collected: " + str(totalmoney_departure[1]) + "  Price: $25/ticket" + "           Time: 12:00  Tickets remaining: " + str(passenger_left_return[1]) + "  Money collected: " + str(totalmoney_return[1]) + "  Price: $25/ticket")
print ("Time: 13:00  Tickets remaining: " + str(passenger_left_departure[2]) + "  Money collected: " + str(totalmoney_departure[2]) + "  Price: $25/ticket" + "           Time: 14:00  Tickets remaining: " + str(passenger_left_return[2]) + "  Money collected: " + str(totalmoney_return[2]) + "  Price: $25/ticket")
print ("Time: 15:00  Tickets remaining: " + str(passenger_left_departure[3]) + "  Money collected: " + str(totalmoney_departure[3]) + "  Price: $25/ticket" + "           Time: 16:00  Tickets remaining: " + str(passenger_left_return[3]) + "  Money collected: " + str(totalmoney_return[3]) + "  Price: $25/ticket\033[0m")
print("")
################################################# Task 2 #################################################
############################################## Purchasing tickets ########################################

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
                x = 1
            if (x == 1 and int(numoftickets) <= 480):
                
                numoftickets = int(numoftickets)
            else:
                print ("Please enter a number, in a reasonable ticket availablity range, properly next time\nSo I'm restarting the questions for you")
                validcheck = True
                continue
            
            ############## Group ##################
            if (numoftickets > 1):    
                print ("Group ticket selected")
                #Departure time
                # wantsdeparttime = input("When do you want to go for departure to the top of the mountain?\n")
                # wantsdeparttime = wantsdeparttime.strip()
                #Validate that tickets are available for departure
                purchasedticket = False

                #First letter of numoftickets
                if (numoftickets<=80 and numoftickets>=10):
                    discout = str(numoftickets) #Notice the spellings of discout and discount
                    discount = int(discout[0])
                    print (discount, "of your tickets will be discounted.")
                else:
                    discount = 0
                
                while (purchasedticket == False):
                    wantsdeparttime = input("When do you want to go for departure to the top of the mountain?\n")
                    wantsdeparttime = wantsdeparttime.strip()
                    if (wantsdeparttime == "09:00" and passenger_left_departure[0] != "Closed"):
                        if (passenger_left_departure[0]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_departure[0] = passenger_left_departure[0] - numoftickets
                            totalmoney_departure[0] = totalmoney_departure[0] + (numoftickets-discount)*25
                            if (passenger_left_departure[0] == 0):
                                passenger_left_departure[0] = "Closed"
                    elif (wantsdeparttime == "11:00" and passenger_left_departure[1] !="Closed"):
                        if (passenger_left_departure[1]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_departure[1] = passenger_left_departure[1] - numoftickets
                            totalmoney_departure[1] = totalmoney_departure[1] + (numoftickets-discount)*25
                            if (passenger_left_departure[1] == 0):
                                passenger_left_departure[1] = "Closed"
                    elif (wantsdeparttime == "13:00" and passenger_left_departure[2] != "Closed"):
                        if (passenger_left_departure[2]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_departure[2] = passenger_left_departure[2] - numoftickets
                            totalmoney_departure[2] = totalmoney_departure[2] + (numoftickets-discount)*25
                            if (passenger_left_departure[2] == 0):
                                passenger_left_departure[2] = "Closed"
                    elif (wantsdeparttime == "15:00" and passenger_left_departure[3] != "Closed"):
                        if (passenger_left_departure[3]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_departure[3] = passenger_left_departure[3] - numoftickets
                            totalmoney_departure[3] = totalmoney_departure[3] + (numoftickets-discount)*25
                            if (passenger_left_departure[3] == 0):
                                passenger_left_departure[3] = "Closed"
                    else:
                        print ("\033[1;31;40mDeparture ticket purchase failed, either due to one of the reasons below:\n•Not enough tickets available for that time slot\n•You entered such a time slot that does not exist\033[0m")
                #Return time
                #Validate that tickets are available for return
                purchasedticket = False
                while (purchasedticket == False):
                    wantsreturntime = input("When do you want to return from the top of the mountain?\n")
                    wantsreturntime = wantsreturntime.strip()            
                    if (wantsreturntime == "10:00" and passenger_left_return[0] != "Closed" and wantsdeparttime != "11:00" and wantsdeparttime != "13:00" and wantsdeparttime != "15:00"):
                        if (passenger_left_return[0]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_return[0] = passenger_left_return[0] - numoftickets
                            totalmoney_return[0] = totalmoney_return[0] + (numoftickets-discount)*25
                            if (passenger_left_return[0] == 0):
                                passenger_left_return[0] = "Closed"
                    elif (wantsreturntime == "12:00" and passenger_left_return[1] != "Closed" and wantsdeparttime != "13:00" and wantsdeparttime != "15:00"):
                        if (passenger_left_return[1]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_return[1] = passenger_left_return[1] - numoftickets
                            totalmoney_return[1] = totalmoney_return[1] + (numoftickets-discount)*25
                            if (passenger_left_return[1] == 0):
                                passenger_left_return[1] = "Closed"
                    elif (wantsreturntime == "14:00" and passenger_left_return[2] != "Closed" and wantsdeparttime != "15:00"):
                        if (passenger_left_return[2]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_return[2] = passenger_left_return[2] - numoftickets
                            totalmoney_return[2] = totalmoney_return[2] + (numoftickets-discount)*25
                            if (passenger_left_return[2] == 0):
                                passenger_left_return[2] = "Closed"
                    elif (wantsreturntime == "16:00" and passenger_left_return[3] != "Closed"):
                        if (passenger_left_return[3]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_return[3] = passenger_left_return[3] - numoftickets
                            totalmoney_return[3] = totalmoney_return[3] + (numoftickets-discount)*25
                            if (passenger_left_return[3] == 0):
                                passenger_left_return[3] = "Closed"
                    else:
                        print ("\033[1;31;40mDeparture ticket purchase failed, either due to one of the reasons below:\n•Not enough tickets available for that time slot\n•You entered such a time slot that does not exist\033[0m")
                


            ################# Single #######################
            elif (numoftickets == 1):
                
                print ("Single ticket selected.")
                #Validate that tickets are available for departure
                purchasedticket = False
                while (purchasedticket == False):
                    wantsdeparttime = input("When do you want to go for departure to the top of the mountain?\n")
                    wantsdeparttime = wantsdeparttime.strip()
                    if (wantsdeparttime == "09:00" and passenger_left_departure[0] != "Closed"):
                        if (passenger_left_departure[0]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_departure[0] = passenger_left_departure[0] - numoftickets
                            totalmoney_departure[0] = totalmoney_departure[0] + numoftickets*25
                            if (passenger_left_departure[0] == 0):
                                passenger_left_departure[0] = "Closed"
                    elif (wantsdeparttime == "11:00" and passenger_left_departure[1] !="Closed"):
                        if (passenger_left_departure[1]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_departure[1] = passenger_left_departure[1] - numoftickets
                            totalmoney_departure[1] = totalmoney_departure[1] + numoftickets*25
                            if (passenger_left_departure[1] == 0):
                                passenger_left_departure[1] = "Closed"
                    elif (wantsdeparttime == "13:00" and passenger_left_departure[2] != "Closed"):
                        if (passenger_left_departure[2]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_departure[2] = passenger_left_departure[2] - numoftickets
                            totalmoney_departure[2] = totalmoney_departure[2] + numoftickets*25
                            if (passenger_left_departure[2] == 0):
                                passenger_left_departure[2] = "Closed"
                    elif (wantsdeparttime == "15:00" and passenger_left_departure[3] != "Closed"):
                        if (passenger_left_departure[3]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_departure[3] = passenger_left_departure[3] - numoftickets
                            totalmoney_departure[3] = totalmoney_departure[3] + numoftickets*25
                            if (passenger_left_departure[3] == 0):
                                passenger_left_departure[3] = "Closed"
                    else:
                        print ("\033[1;31;40mDeparture ticket purchase failed, either due to one of the reasons below:\n•Not enough tickets available for that time slot\n•You entered such a time slot that does not exist\033[0m\n")
                #Return time
                #Validate that tickets are available for return
                purchasedticket = False
                while (purchasedticket == False):
                    wantsreturntime = input("When do you want to return from the top of the mountain?\n")
                    wantsreturntime = wantsreturntime.strip()
                    if (wantsreturntime == "10:00" and passenger_left_return[0] != "Closed" and wantsdeparttime != "11:00" and wantsdeparttime != "13:00" and wantsdeparttime != "15:00"):
                        if (passenger_left_return[0]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_return[0] = passenger_left_return[0] - numoftickets
                            totalmoney_return[0] = totalmoney_return[0] + numoftickets*25
                            if (passenger_left_return[0] == 0):
                                passenger_left_return[0] = "Closed"
                    elif (wantsreturntime == "12:00" and passenger_left_return[1] != "Closed" and wantsdeparttime != "13:00" and wantsdeparttime != "15:00"):
                        if (passenger_left_return[1]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_return[1] = passenger_left_return[1] - numoftickets
                            totalmoney_return[1] = totalmoney_return[1] + numoftickets*25
                            if (passenger_left_return[1] == 0):
                                passenger_left_return[1] = "Closed"
                    elif (wantsreturntime == "14:00" and passenger_left_return[2] != "Closed" and wantsdeparttime != "15:00"):
                        if (passenger_left_return[2]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_return[2] = passenger_left_return[2] - numoftickets
                            totalmoney_return[2] = totalmoney_return[2] + numoftickets*25
                            if (passenger_left_return[2] == 0):
                                passenger_left_return[2] = "Closed"
                    elif (wantsreturntime == "16:00" and passenger_left_return[3] != "Closed"):
                        if (passenger_left_return[3]>=numoftickets):
                            print ("\033[1;32;40mDeparture tickets successfully purchased\033[0m")
                            purchasesuccess = True
                            purchasedticket = True
                            passenger_left_return[3] = passenger_left_return[3] - numoftickets
                            totalmoney_return[3] = totalmoney_return[3] + numoftickets*25
                            if (passenger_left_return[3] == 0):
                                passenger_left_return[3] = "Closed"
                    else:
                        print ("\033[1;31;40mDeparture ticket purchase failed, either due to one of the reasons below:\n•Not enough tickets available for that time slot\n•You entered such a time slot that does not exist\n•Chosen return time is before the departure time, which is impossible\033[0m\n")
            
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
        
        print ("\n\033[1;34;40mTrain times and remaining tickets along with price are shown below:")
        print ("Departure to top of mountain                                                         Return from top of mountain")
        print ("Time: 09:00  Tickets remaining: " + str(passenger_left_departure[0]) + "  Money collected: " + str(totalmoney_departure[0]) + "  Price: $25/ticket" + "           Time: 10:00  Tickets remaining: " + str(passenger_left_return[0]) + "  Money collected: " + str(totalmoney_return[0]) + "  Price: $25/ticket")
        print ("Time: 11:00  Tickets remaining: " + str(passenger_left_departure[1]) + "  Money collected: " + str(totalmoney_departure[1]) + "  Price: $25/ticket" + "           Time: 12:00  Tickets remaining: " + str(passenger_left_return[1]) + "  Money collected: " + str(totalmoney_return[1]) + "  Price: $25/ticket")
        print ("Time: 13:00  Tickets remaining: " + str(passenger_left_departure[2]) + "  Money collected: " + str(totalmoney_departure[2]) + "  Price: $25/ticket" + "           Time: 14:00  Tickets remaining: " + str(passenger_left_return[2]) + "  Money collected: " + str(totalmoney_return[2]) + "  Price: $25/ticket")
        print ("Time: 15:00  Tickets remaining: " + str(passenger_left_departure[3]) + "  Money collected: " + str(totalmoney_departure[3]) + "  Price: $25/ticket" + "           Time: 16:00  Tickets remaining: " + str(passenger_left_return[3]) + "  Money collected: " + str(totalmoney_return[3]) + "  Price: $25/ticket\033[0m")

################################################# Task 3 #################################################
############################################# End of the day #############################################

print ("We have reached the end of the day! So down below are the total money taken and the passengers travelled on each train journey.")

print ("\033[1;34;40mDeparture to top of mountain                                                         Return from top of mountain")
print ("Time: 09:00  Passengers travelled: " + str(480-passenger_left_departure[0]) + "  Money collected: " + str(totalmoney_departure[0]) + "  Price: $25/ticket" + "           Time: 10:00  Passengers travelled: " + str(480-passenger_left_return[0]) + "  Money collected: " + str(totalmoney_return[0]) + "  Price: $25/ticket")
print ("Time: 11:00  Passengers travelled: " + str(480-passenger_left_departure[1]) + "  Money collected: " + str(totalmoney_departure[1]) + "  Price: $25/ticket" + "           Time: 12:00  Passengers travelled: " + str(480-passenger_left_return[1]) + "  Money collected: " + str(totalmoney_return[1]) + "  Price: $25/ticket")
print ("Time: 13:00  Passengers travelled: " + str(480-passenger_left_departure[2]) + "  Money collected: " + str(totalmoney_departure[2]) + "  Price: $25/ticket" + "           Time: 14:00  Passengers travelled: " + str(480-passenger_left_return[2]) + "  Money collected: " + str(totalmoney_return[2]) + "  Price: $25/ticket")
print ("Time: 15:00  Passengers travelled: " + str(480-passenger_left_departure[3]) + "  Money collected: " + str(totalmoney_departure[3]) + "  Price: $25/ticket" + "           Time: 16:00  Passengers travelled: " + str(480-passenger_left_return[3]) + "  Money collected: " + str(totalmoney_return[3]) + "  Price: $25/ticket\033[0m")


#Just a newline to make output look nicer
print ("")
