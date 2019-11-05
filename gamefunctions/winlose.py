from random import randint

#defining a variable
def winolose(status):
	global clives 
	global plives 
	global choices
	global computer
	global player 

	print ("\n\n \033[34m ----------------------------------------------------\033[30;0;0m" )
	print ("\n\n     You ", status )
	print ("      Would you like to play again? \n")
	choice = input ("                Y / N \n")

	if (choice == "N" or choice == "n"):
		print ("\n\n\n              Thank you for playing!\n\n\n")
		exit ()

	elif (choice == "Y" or choice == "y"):
		print ("\n\n Preparing to start again... ")
		plives = 5
		clives = 5

	else:
		print ("E")