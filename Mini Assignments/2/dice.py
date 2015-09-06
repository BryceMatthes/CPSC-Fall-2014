# Name: Bryce Matthes	
# Student ID: 10147880

import random # Imports random to be used for the dice roll

def letterGrade(number):
	if (number == 1):
		print("W")
	elif (number == 2):
		print("F")
	elif (number == 3):
		print("D")
	elif (number == 4):
		print("C")
	elif (number == 5):
		print("B")
	elif (number == 6):
		print("A")
	elif (number > 6):
		print("Error: High")
	elif (number < 1):
		print("Error: Low")							

roll = random.randrange(1,7,1) # 6 numbers starting at 1 (1-6)

letterGrade(roll)