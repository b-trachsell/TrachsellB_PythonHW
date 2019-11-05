from random import randint
import time
from gamefunctions import winlose, compare
#Choices is an array, an array is a container that can hold multiple values

choices = ["rock", "paper", "scissors"]
computer = choices[randint (0, 2)]
pwin = ("\033[32m            ** Player wins! ** \033[30;0;0m")
cwin = ("\033[31m            ** Comp wins! ** \033[30;0;0m")
plives = 5
clives = 5
player = False
#State variables



print ("\n\n\n\n\n\033[35m * * * * Welcome to Rock Paper Scissors in Python! * * * * \033[30;0;0m")
# Prints before the loop so it only shows once.


# set up the game loop
# Loops the game until someone wins
while player == False:

	print ("\n\n \033[34m ------------------------------------------------\033[30;0;0m" )
	time.sleep(1.5)
	# Separates each round and delays the next round for easier reading of last rounds results
	
	print( "\n\n          Player lives:", plives, "/5\n")
	print( "          Computer lives:", clives, "/5\n")
	# Displays player and computer life totals
	
	player = input ("\n\n    Choose rock, paper, or scissors\n\n                 ")
	player = player.lower()
	# Asks for the users input, and sets to lowercase

	if ( player == "quit" ):
		exit()
		print ("\n\n\n")
		#Checks if the player wants to quit before any game happens
		#Prints a few lines for replay clarity

	print( "\n \033[31m      computer chose:    ", computer)
	print("\033[32m       player chose:      ", player,"\n \033[30;0;0m")
	#displays what each player chose, if the player did not choose quit
	
	#proceeds to check who the winner is, and prints the result
	

	compare.comparing(player, computer)

	# if ( player == computer ):
	# 	print ("  You and the computer chose the same! \n")
	# 	print ( "\033[35m            ** Tie! **\033[30;0;0m" )

	# elif ( player == "rock" ):
	# 	if (computer == "paper"):
	# 		print ("           Paper covers rock! \n")
	# 		print (cwin)
	# 		plives = plives - 1

	# 	elif (computer == "scissors"):
	# 		print ("          Rock smashes scissors! \n")
	# 		print (pwin)
	# 		clives = clives - 1

	# elif ( player == "paper"):
	# 	if (computer == "rock"):
	# 		print ("           Paper covers rock! \n")
	# 		print (pwin)
	# 		clives = clives - 1

	# 	elif (computer == "scissors"):
	# 		print ("           Scissors cut paper! \n")
	# 		print (cwin)
	# 		plives = plives - 1


	# elif ( player == "scissors" ):
	# 	if ( computer == "paper"):
	# 		print ("           Scissors cut paper! \n")
	# 		print (pwin)
	# 		clives = clives - 1

	# 	elif (computer == "rock"):
	# 		print ("          Rock smashes scissors! \n")
	# 		print (cwin)
	# 		plives = plives - 1

	# else:
	# 	print ("     Sorry, that's not a valid answer! ")
	# 	#if an answer is not rock paper or scissors.
		

	if plives == 0:
		winlose.winolose(" lose!")

	if clives == 0:
		winlose.winolose(" win!")	


	# if (plives is 0):
	# 	#if either the player lives or computer lives reach 0:

	# 	print ("\n\n \033[34m ----------------------------------------------------\033[30;0;0m" )
	# 	print ("\n\n     You lose, You are out of lives! " )
	# 	print ("      Would you like to play again? \n")
	# 	choice = input ("                Y / N \n")

	# 	if (choice == "N" or choice == "n"):
	# 		print ("\n\n\n              Thank you for playing!\n\n\n")
	# 		exit ()

	# 	elif (choice == "Y" or choice == "y"):
	# 		print ("\n\n Preparing to start again... ")
	# 		plives = 5
	# 		clives = 5

	# 	else :
	# 		print ("E")
			
	# elif (clives is 0):

	# 	print ("\n\n \033[34m ----------------------------------------------------\033[30;0;0m" )
	# 	print ("\n\n   You Win, Your opponent is out of lives!" )
	# 	print ("        Would you like to play again? \n")
	# 	choice = input ("                  Y / N \n")

	# 	if (choice == "N" or choice == "n"):
	# 		print ("\n\n\n              Thank you for playing!\n\n\n")
	# 		exit ()

	# 	elif (choice == "Y" or choice == "y"):
	# 		print ("\n\n Preparing to start again... ")
	# 		plives = 5
	# 		clives = 5

	# 	else:
	# 		print ("E")	
	
	player = False
	computer = choices[randint (0, 2)]
	#resets player value to restart the loop, and picks a new weapon for the computer

