import time
from random import randint
from gamefunctions import config

#config.computer = config.nconfig.computer
#config.pwin = config.nconfig.pwin
#config.cwin = config.nconfig.cwin
#config.plives = config.nconfig.plives
#config.clives = config.nconfig.clives
#config.player = config.nconfig.player

print ("hello")
print (config.player)

def comparing ():
        
        
	if ( config.player == config.computer ):
		print ("  You and the computer chose the same! \n")
		print ( "\033[35m            ** Tie! **\033[30;0;0m" )

	elif ( config.player == "rock" ):
		if (config.computer == "paper"):
			print ("           Paper covers rock! \n")
			print (config.cwin)
			config.plives = config.plives - 1

		elif (config.computer == "scissors"):
			print ("          Rock smashes scissors! \n")
			print (config.pwin)
			config.clives = config.clives - 1

	elif ( config.player == "paper"):
		if (config.computer == "rock"):
			print ("           Paper covers rock! \n")
			print (config.pwin)
			config.clives = config.clives - 1

		elif (config.computer == "scissors"):
			print ("           Scissors cut paper! \n")
			print (config.cwin)
			config.plives = config.plives - 1


	elif ( config.player == "scissors" ):
		if ( config.computer == "paper"):
			print ("           Scissors cut paper! \n")
			print (config.pwin)
			config.clives = config.clives - 1

		elif (config.computer == "rock"):
			print ("          Rock smashes scissors! \n")
			print (config.cwin)
			config.plives = config.plives - 1

	else:
		print ("     Sorry, that's not a valid answer! ")
		#if an answer is not rock paper or scissors.
		
