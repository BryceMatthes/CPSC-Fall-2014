# Name: Bryce Matthes	
# Student ID: 10147880
import random
import math

def getHours():
	'''
	This function is used to get the number of hours to study and the number of hours for fun from the user.
	The prompt will continue to display until values within the allowed range and input (20 hours total). It
	also offers an option to reinput the values if the user made a mistake.
	'''
	cHours = False
	while(cHours == False):
		complete = False
		while(complete != True):
			studyHours = input("Please choose how many hours you want to study: ")
			if ((int(studyHours) > 20) or (int(studyHours) < 0)): # Checks if the users input is within the range
				print("Please try again. (0-20)")
			else:
				complete = True

		hoursLeft = (20 - int(studyHours))
		complete = False

		while(complete != True):
			print()
			print("--You have " +str(hoursLeft) +" hours left to invest--") # Tells the user how many ours are left /20
			print()
			funHours = input("Please choose how many hours you want towards fun: ")
			if ((int(funHours) > int(hoursLeft)) or (int(funHours) < int(hoursLeft))):
				print("Plesae try again.")
			else:
				complete = True
		print("------------------------")		
		print("You have invested " +str(studyHours) +" hours into studying & invested " +str(funHours) +" hours into fun.")
		reinput = input("Would you like to re-input these values? \nPress '1' to try again, if not press any other number: ") 
		if int(reinput) != 1: # iff the user inputs (1) the user will be reprompted for fun & study hours
			cHours = True
			return(studyHours, funHours) # Sends back the who values for gpaRange to use next.

def gpaRange(rng):
	'''
	using the values from the table on http://pages.cpsc.ucalgary.ca/~tamj/231/assignments/assignment2/index.htm
	this function uses the random number from 1-100 to choose the grapdepoint value dependant on the range.
	'''
	##print("DEBUG:" +str(rng))
	if ((int(studyHours) >= 18)): # If the random number is >= than 18
		if rng >= 61:
			gradepoint = 4
		elif rng >= 36:
			gradepoint = 3
		elif rng >= 11:
			gradepoint = 2
		elif rng >= 6:
			gradepoint = 1
		elif rng <= 5:
			gradepoint = 0
	elif ((int(studyHours) >= 10)): # If the random number is < 20 and the number is >= 10
		if rng >= 81:
			gradepoint = 4
		elif rng >= 61:
			gradepoint = 3
		elif rng >= 41:
			gradepoint = 2
		elif rng >= 21:
			gradepoint = 1
		elif rng <= 20:
			gradepoint = 0		
	elif ((int(studyHours) >= 1)): # If the random number is < 10 and the number is >= 1
		if rng >= 96:
			gradepoint = 4
		elif rng >= 91:
			gradepoint = 3
		elif rng >= 66:
			gradepoint = 2
		elif rng >= 41:
			gradepoint = 1
		elif rng <= 40:
			gradepoint = 0
	else:						   # If the random number is < 1
		if rng >= 51:
			gradepoint = 1
		elif rng <= 50:
			gradepoint = 0
	return gradepoint		

def intro():
	'''
	I am not sure if I should be using more than one print to show a large
	amount of text to the user. I am using "\n" to display new lines off the
	same print function. 
	'''
	print("#### Welcome to my Life Satisfaction Program #####")
	print()
	print("This program works by taking the hours you spend studying and the hours you\nspend having fun (out of 20). Using these two values the program generates\na number for your GPA within a range determined by your study hours and adds\nyour 'Fun points' (determined by (fun hours)/6 and rounded up at .5) \nwith your GPA to show how satisfied you are with life.")
	print()

intro() # Runs the intro text
studyHours, funHours = getHours() # Gets values of studyHours and funHours from the user		
rng = random.randrange(1,101,1) # 100 numbers starting at 1 (1-100)
gradepoint = gpaRange(rng) # Runs gpaRange to find the number for GPA
rFunAdd = round(int(funHours)/6) # Rounding and calculating 'fun points'
print()
print("Your GPA is " +str(gradepoint) +" and your fun points are: " +str(rFunAdd))
satPoints = int(gradepoint) + int(rFunAdd) # Satisfaction points are (funpoints + gradepoints)
print("Satisfaction points: " +str(satPoints))
