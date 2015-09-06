# Title: Bryce's GPA Calculator
# Your name: Bryce Matthes	
# Student ID: 10147880
# Tutorial: T07
# Assignment (1)

print()
print("Welcome to my GPA Calculator")
print("Please input values in GPA format (4.0 scale)")
print()
print("==Mini Assignments==") #This prints a title
print()
miniOne = input("What was your mark on Mini Assignment 1? (1%): ")
miniTwo = input("What was your mark on Mini Assignment 2? (1%): ")
miniThree = input("What was your mark on Mini Assignment 3? (1%): ")
miniTotal = (((float(miniOne) + float(miniTwo) + float(miniThree))/(4.0*3))*.06) # By taking all the values input and turning them into terms of 100% we can calculate weighted averages
print()
print("==Full Assignments==") # Title
print()
fullOne = input("What was your mark on Full Assignment 1? (4%): ")
fullTwo = input("What was your mark on Full Assignment 2? (5%): ")
fullThree = input("What was your mark on Full Assignment 3? (6%): ")
fullFour = input("What was your mark on Full Assignment 4? (7%): ")
fullFive = input("What was your mark on Full Assignment 5? (7%): ")
fullTotal = (((float(fullOne)/(4.0))*.04) + ((float(fullTwo)/(4.0))*.05) + (float(fullThree)/(4.0)*.06) + ((float(fullFour)/(4.0))*.07) + ((float(fullFive)/(4.0))*.07)) # Takes the value of each input value and turns them into their respective average out of 100%
print()
print("==Examination Marks==") # Title
print()
examOne = input("What was your mark on your Midterm Examination? (25%): ")
examTwo = input("What was your mark on your Final Examination? (40%): ")
examTotal = (((float(examOne)/(4.0))*.25) + ((float(examTwo)/(4.0))*.40))
midtermW = (float(examOne)/(4.0))*.25 #Used as the midterm gpa value in the final print
finalW = (float(examTwo)/(4.0))*.40	  #Used as the final exams gpa in the final print
gpaTotal = (float(examTotal) + float(fullTotal) + float(miniTotal)) # Combining the totals of all the 4 
gpaTotal = float(gpaTotal)*4.0 #Because the calculations were all done to the GPA form being in terms of 1 (or 100%) this turns the value back to the 4.0 GPA average instead of 100%
print()
print() # This is where the final output begins. It is formatted to two decimal places.
print("Weighted mini assignment grade: ", end='') #end is used to keep the next line's print (used to format output) on this line.
print("%3.2f" % (miniTotal*4)) #Used to suppress the output to 3 digits, two of which are decimals 
print("Weighted assignment grade: ", end='')
print("%3.2f" % (fullTotal*4))
print("Weighted midterm grade: ", end='')
print("%3.2f" % (midtermW*4))
print("Weighted final exam grade: ", end='')
print("%3.2f" % (finalW*4))
print("Weighted term grade: ", end='')
print("%3.2f" % (gpaTotal))
print()
print("Thank you for using my GPA calculator.") #End of program
