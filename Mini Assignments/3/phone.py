# Your name: Bryce Matthes	
# Student ID: 10147880
# Tutorial #: T07

complete = False
i = 0 #Just a counter 

while complete == False:
	pNumber = input("Please enter your phone number: ")
	pLength = 0 #Resets pLength every time
	for i in pNumber: #This is used to check the length of what the user entered
		pLength += 1	
	for i in pNumber:
		if int(pLength) > 7: #Error for too many digits in phone number
			print()
			print("Error: Too Many Digits!")
			print("Your phone number was: " +str(pLength))			
			print("Phone numbers must 7 digits. Please try again")
			print()
			break
		if int(pLength) < 7: #Error for too few digits in phone number
			print()
			print("Error: Too Few Digits!")
			print("Your phone number was: " +str(pLength))			
			print("Phone numbers must 7 digits. Please try again")
			print()
			break	
		if (int(i) == 0): #Error for the phone number starting with a 0
			print()
			print("Your number can't start with 0. please try again.")
			print()
			break
		else:
			complete = True
print("Thank you. valid phone number entered.")
print("COMPLETE")	