# Your name: Bryce Matthes	
# Student ID: 10147880
# Tutorial #: T07
# Version: 1.0
# LC: 83

'''
Tam's simulated life forms is a 'dating' simulation, The user
decides what the Target will have for X rolls - from 1-100%.

The program tries to make itself roll X when the Target does and
Y whene the Target does.

The Pursuer will adjust itself to try and match the Target's X and Y percent

List of features: Every feature is implemented and complete. (14/14)

'''

##Import Target and Pursuer
from Pursuer import Pursuer
from Target import Target
			
def main():

	counter = 0
	success = 0
	matchCheck = ""

	while True:
		try:
			interactionsNum = int(input("Enter the number of interactions (1 or greater): "))
			if interactionsNum <= 0:
				print("Number must be 1 or greater") ##For 1 or greater
			else:
				break
		except ValueError:
			print("Do not enter non-numeric values") ##For non-numeric

	while True:
		try:
			xPercent = int(input("Enter the percentage # of 'X' interactions for target (whole numbers from 0 - 100):"))
			if xPercent < 0 or xPercent > 100:
				print("Enter a value between 0 - 100 only") ##Sub one and greater than 100
			else:
				break
		except ValueError:
			print("Do not enter non-numeric values") ##Non-numeric

	targetCall = Target() #Makes a Target
	pursuerCall = Pursuer() #Makes a Pursuer
	targetCall.setPercents(xPercent) #Set Target to user input

	##Start run interactions
	while counter < interactionsNum:
		targetVal = targetCall.runRandom()
		pursuerVal = pursuerCall.runRandom()
		if targetVal == pursuerVal:
			matchCheck = "Matched behavior"
			success += 1
		elif (targetVal == "x" and pursuerVal == "y"):
			pursuerCall.setPercents(5) #Set X percent up 
			matchCheck = "Mis-Matched behavior"
		else:
			pursuerCall.setPercents(-5)
			matchCheck = "Mis-Matched behavior"	

		print("Target: "+targetVal +" | Pursuer:" +pursuerVal +" | " +matchCheck) #Display interaction Target and Pursuer
		counter += 1
	print()
	print()

	##Begin post run display	
	print("ANALYSIS OF ALL THE INTERACTIONS (THE DATE)")
	print(" Target: No. of X's: "+str(targetCall.xCount) +"\tNo. of Y's: "+str(targetCall.yCount))
	print("Pursuer: No. of X's: "+str(pursuerCall.xCount) +"\tNo. of Y's: "+str(pursuerCall.yCount))
	print("Number of successful matches: "+str(success))
	print("Proportion of successful matches: " +"{0:0.1f}".format((success/interactionsNum)*100) +"%")
	print()
	if (success/interactionsNum)*100 >= 50:
		print("Date was successful <3")
	else:
		print("Date was unsuccessful </3")

main()		