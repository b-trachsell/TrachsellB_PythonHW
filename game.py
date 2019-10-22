from random import randint


#Choices is an array, an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]
computer = choices[randint (0, 2)]
player = False

# set up the game loop 
while player == False:

	player = input ("\nChoose rock, paper, or scissors\n")
	print( "\ncomputer chose,", computer)
	print("player chose", player,"\n")


	if ( player == computer ):
		print ( "Tie" )

	elif ( player == "quit" ):
		exit()

	elif ( player == "rock" and computer == "paper"):
		print (" ** comp wins ** ")

	elif ( player == "rock" and computer == "scissors"):
		print (" ** player wins ** ")

	elif ( player == "paper" and computer == "rock"):
		print (" ** player wins ** ")

	elif ( player == "paper" and computer == "scissors"):
		print (" ** comp wins ** ")

	elif ( player == "scissors" and computer == "paper"):
		print (" ** player wins ** ")

	elif ( player == "scissors" and computer == "rock"):	
		print (" ** comp wins ** ")

	else:
		print ("E")


	player = False
	computer = choices[randint (0, 2)]

