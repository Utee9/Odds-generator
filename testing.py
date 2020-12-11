import random
import numpy

oddslist = []
randomlist = []
userodds = float()
userlist = []
xodds= float()

n = int(input("Enter number of games: "))

for i in range (n):
        print ("Enter the next number: ")
        oddslist.append(float(input("")))

 
def random_list():
        m = int(input("Enter the number of random odds to produce: "))

        for i in range (m): 
                rand_val = random.choice(oddslist) 
                if rand_val in randomlist:
                        continue
                else:
                        randomlist.append(rand_val)
        print ("Your random list is: ", randomlist)

def user_odds():
        maximumodds = float(numpy.prod(oddslist))
        print ("Your total maximum odds is: ", maximumodds)
        userodds = float(input("Enter the total odds you want: "))
        
        if userodds > maximumodds:
                print ("Your desired odds is more than your maximum odds")
                 
        else:             
                runtime = 0
                while True:
                        rand_val= random.choice(oddslist)
                        if rand_val in userlist:
                                continue
                        else:
                                userlist.append(rand_val) 
                        xodds = float(numpy.prod(userlist))
                        if xodds > userodds:
                                break
                        else:
                                runtime+=1
                                continue
                print ("Your odds total is: ", xodds)
                print("Your desired list is: ", userlist)

def intro():
        answer = int(input("Enter '1' to create a random odds list, press '2' to generate odds: "))
        if answer==1:
                random_list()
        elif answer==2:
                user_odds()
        else:
                print("Are you dumb?  \n or stupid? \n or dumb uhn?")
                intro()

intro()
