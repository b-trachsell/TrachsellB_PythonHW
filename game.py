from random import randint
import time
from gamefunctions import winlose, compare, config
#config.choices is an array, an array is a container that can hold multiple values

#config.choices = config.nconfig.choices
#config.computer = config.nconfig.computer
#config.pwin = config.nconfig.pwin
#config.cwin = config.nconfig.cwin
#config.plives = config.nconfig.plives
#config.clives = config.nconfig.clives
#config.player = config.nconfig.player
#State variables



print ("\n\n\n\n\n\033[35m * * * * Welcome to Rock Paper Scissors in Python! * * * * \033[30;0;0m")
# Prints before the loop so it only shows once.


# set up the game loop
# Loops the game until someone wins
while config.player == False:

	print ("\n\n \033[34m ------------------------------------------------\033[30;0;0m" )
	time.sleep(1.5)
	# Separates each round and delays the next round for easier reading of last rounds results
	
	print( "\n\n          player lives:", config.plives, "/5\n")
	print( "          computer lives:", config.clives, "/5\n")
	# Displays config.player and config.computer life totals
	
	config.player = input ("\n\n    Choose rock, paper, or scissors\n\n                 ")
	config.player = config.player.lower()
	# Asks for the users input, and sets to lowercase

	if ( config.player == "quit" ):
		exit()
		print ("\n\n\n")
		#Checks if the config.player wants to quit before any game happens
		#Prints a few lines for replay clarity

	print( "\n \033[31m      computer chose:    ", config.computer)
	print("\033[32m       player chose:      ", config.player,"\n \033[30;0;0m")
	#displays what each config.player chose, if the config.player did not choose quit
	
	#proceeds to check who the winner is, and prints the result
	

	compare.comparing()

	# if ( config.player == config.computer ):
	# 	print ("  You and the config.computer chose the same! \n")
	# 	print ( "\033[35m            ** Tie! **\033[30;0;0m" )

	# elif ( config.player == "rock" ):
	# 	if (config.computer == "paper"):
	# 		print ("           Paper covers rock! \n")
	# 		print (config.cwin)
	# 		config.plives = config.plives - 1

	# 	elif (config.computer == "scissors"):
	# 		print ("          Rock smashes scissors! \n")
	# 		print (config.pwin)
	# 		config.clives = config.clives - 1

	# elif ( config.player == "paper"):
	# 	if (config.computer == "rock"):
	# 		print ("           Paper covers rock! \n")
	# 		print (config.pwin)
	# 		config.clives = config.clives - 1

	# 	elif (config.computer == "scissors"):
	# 		print ("           Scissors cut paper! \n")
	# 		print (config.cwin)
	# 		config.plives = config.plives - 1


	# elif ( config.player == "scissors" ):
	# 	if ( config.computer == "paper"):
	# 		print ("           Scissors cut paper! \n")
	# 		print (config.pwin)
	# 		config.clives = config.clives - 1

	# 	elif (config.computer == "rock"):
	# 		print ("          Rock smashes scissors! \n")
	# 		print (config.cwin)
	# 		config.plives = config.plives - 1

	# else:
	# 	print ("     Sorry, that's not a valid answer! ")
	# 	#if an answer is not rock paper or scissors.
		

	if config.plives == 0:
		winlose.winolose(" lose!")

	if config.clives == 0:
		winlose.winolose(" win!")	


	# if (config.plives is 0):
	# 	#if either the config.player lives or config.computer lives reach 0:

	# 	print ("\n\n \033[34m ----------------------------------------------------\033[30;0;0m" )
	# 	print ("\n\n     You lose, You are out of lives! " )
	# 	print ("      Would you like to play again? \n")
	# 	choice = input ("                Y / N \n")

	# 	if (choice == "N" or choice == "n"):
	# 		print ("\n\n\n              Thank you for playing!\n\n\n")
	# 		exit ()

	# 	elif (choice == "Y" or choice == "y"):
	# 		print ("\n\n Preparing to start again... ")
	# 		config.plives = 5
	# 		config.clives = 5

	# 	else :
	# 		print ("E")
			
	# elif (config.clives is 0):

	# 	print ("\n\n \033[34m ----------------------------------------------------\033[30;0;0m" )
	# 	print ("\n\n   You Win, Your opponent is out of lives!" )
	# 	print ("        Would you like to play again? \n")
	# 	choice = input ("                  Y / N \n")

	# 	if (choice == "N" or choice == "n"):
	# 		print ("\n\n\n              Thank you for playing!\n\n\n")
	# 		exit ()

	# 	elif (choice == "Y" or choice == "y"):
	# 		print ("\n\n Preparing to start again... ")
	# 		config.plives = 5
	# 		config.clives = 5

	# 	else:
	# 		print ("E")	
	
	config.player = False
	config.computer = config.choices[randint (0, 2)]
	
	#resets config.player value to restart the loop, and picks a new weapon for the config.computer

