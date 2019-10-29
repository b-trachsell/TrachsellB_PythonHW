from random import randint


#Choices is an array, an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]
computer = choices[randint (0, 2)]
pwin = ("            ** player wins ** ")
cwin = ("            ** comp wins ** ")
player = False
#State variables


# set up the game loop
# Loops the game until someone wins 
while player == False:

	print ("\n\n \033[31m ----------------------------------------------------\033[30m" )
	player = input ("\n\n  Choose rock, paper, or scissors\n\n             ")
	player = player.lower()
	# Separates games, and begins a new one asking for input, sets input to lowercase

	if ( player == "quit" ):
		exit()
	#Checks if the player wants to quit before any game happens

	print( "\n      computer chose:    ", computer)
	print("      player chose:      ", player,"\n")
	#displays what each player chose
	
	#proceeds to check who the winner is, and prints the result
	if ( player == computer ):
		print ("  You and the computer chose the same! \n")
		print ( "            ** Tie! **" )

	elif ( player == "rock" ):
		if (computer == "paper"):
			print ("          Paper covers rock! \n")
			print (cwin)
		elif (computer == "scissors"):
			print ("          Rock smashes scissors! \n")
			print (pwin)

	elif ( player == "paper"):
		if (computer == "rock"):
			print ("          Paper covers rock! \n")
			print (pwin)
		elif (computer == "scissors"):
			print ("          Scissors cut paper! \n")
			print (cwin)

	elif ( player == "scissors" ):
		if ( computer == "paper"):
			print ("          Scissors cut paper! \n")
			print (pwin)
		elif (computer == "rock"):
			print ("          Rock smashes scissors! \n")
			print (cwin)

	else:
		print ("E")
		#if an answer is not rock paper or scissors.

		#set player back to false to reset the loop, and have comp pick another weapon
	player = False
	computer = choices[randint (0, 2)]

