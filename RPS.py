from random import randint

#Create a list for bot to use RPS
t = ["rock","paper","scissors"]

bot = t[randint(0,2)]
player = False

#print("First test")

while player == False:
    #set player to True
        player = input ("rock, paper, scissors? \nEnter x to exit:")
        if player == bot:
            print("Tie!")
        
        #Player picks rock
        elif player == "rock":
            if bot == "paper":
                print("Bot wins!")
            else:
                print("You Win!")
        
        #Player picks paper
        elif player == "paper":
            if bot == "scissors":
                print("Bot wins!")
            else:
                print("You Win!")
        

        #Player picks scissors
        elif player == "scissors":
            if bot == "rock":
                print("Bot wins!")
            else:
                print("You Win!")

        #Exit program

        elif player == "x":
            print("Bye bye")
            break


        #Input validation here as a clear all solution
        else:
            print("Not a valid play, try again")

        #Since you are adding a value to player it will turn true
        #By making player = False it will loop again

        player = False
        computer = t[randint(0,2)]