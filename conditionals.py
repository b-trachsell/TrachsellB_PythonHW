# Looking at temperature of water and its state



temp = int(input("enter a temperature: "))

if (temp < 4):
	print ("water is frozen")

elif (temp > 4 and temp < 100):
	print ("water is liquid")

elif (temp >= 100):
	print ("water is vapor")

else:
	print(" No")
