# Your name: Bryce Matthes	
# Student ID: 10147880
# Tutorial #: T07
# Version: 0.1
# LC: 202
'''
This program is used to convert files of any extention by taking their
information line by line and editing it based on specific command line
arguments entered by the user. (-v +v -t +t -T(n)) where (n) is an integer
from 2-8

What should be working:

(-v) to remove the visable characters
(+v) to add the visable characters
(-t) to change all spaces length 4 or tab-stops from spaces to tabs -T(4) before the first non-space/tab character
(+t) to change all tabs to 4 space before the first non-space/tab character
(-T(n)) to cange all instances of (n) spaces to tabs (Tab Stops don't work here.)
(-help) or any varient of this commend with any caps/lowercase letters will display the help text. If it is run
with another argument (-help -v) it will display help text then run the other argument.
'''
import sys
EOF = chr(4)

def getInput(): ##Copied
    """This function works exactly like input() (with no arguments), except that,
    instead of throwing an exception when it encounters EOF (End-Of-File), 
    it will return an EOF character (chr(4)).
    Returns: a line of input or EOF if EOFError occurs during input.
    """ 
    try:
        ret = input()
    except EOFError:
        ret = EOF
    return ret

def getArgs():
	'''
	Used to check the arguments the user wants to run for each line.
	takes care of printing and getting new lines.
	'''
	counter = 1
	fileContent = getInput() ##Gets the next/first line
	if (fileContent != EOF):
		for arg in sys.argv: ##checks all args
			if (counter == 1):
				counter = counter + 1
			else:
				fileContent = argRun(arg,fileContent) ##using argRun is creates a new fileContent of modified content
		print(fileContent)
		getArgs()	##Runs on every line until EOF		
			
def main():
	'''
	Runs to first check for error and tells the prgram to run or not.
	'''
	counter = 1
	Error = False
	runArgs = False
	helpError = False
	criticalError = False
	stringTest = ""
	for arg in sys.argv:
		if (counter == 1):
			counter = counter + 1
		else:
			counter = counter + 1
			argUp = arg.upper()
			if (arg[:2] == "-T" and (int(arg[2:]) > 8 or int(arg[2:]) < 2)):
				print("The -T qualifier must be immediately followed by an integer: "+arg)
				Error = True	
			if ((arg[:2] == "-H" or arg[:2] == '-h') and (argUp == '-H' or argUp == '-HE' or argUp == '-HEL' or argUp == '-HELP')): ##For all of -Help/-help/-h
				helpError = True
			elif not (arg[:2] in '-v+v-t+t-T'): ##Checking for unrecognized arguments
				print("Unrecognized argument: "+arg)
				Error = True					
			stringTest = stringTest + arg ##stringTest is used to save a combined string or all arguments		
	if (("-v" in stringTest) and ("+v" in stringTest)):
		print("Qualifiers +v and -v cannot both be used together.")
		Error = True
		criticalError = True	
	if (("-t" in stringTest) and ("+t" in stringTest)):
		print("Qualifiers +t and -t cannot both be used together.")
		Error = True
		criticalError = True		
	if Error == True or helpError == True:
  		print("Synopsis:\
   \n\ttabs [+t] [-t] [-T<integer>] [+v] [-v] [-help]\
     \n\t\t+t    -replaces prefix sequences of spaces of length T with a single tab \
     \n\t\t-t    -replaces prefix tabs with sequences of T spaces\
     \n\t\t-T<integer> -the <integer> defines the space-to-tab ratio, T (default=4) \
     \n\t\t+v    -changes all spaces, tabs, and newlines to printable (visible) characters \
     \n\t\t-v    -undoes the effects of +v \
     \n\t\t-help -prints out this help text \
  \n\t+t and -t are incompatible \
  \n\t+v and -v are incompatible")						
	else:
		runArgs = True
		getArgs()
	if (helpError == True and criticalError != True and counter > 3 and Error != True and runArgs == False): ##Running the program if there is -help and other non-error command
		getArgs()	
		
def argRun(userArgument,fileContent):
	'''
	This funcation is used to run the command on the line and returns the string back.
	'''
	if userArgument == ("-t"):
		return(removeTabs(fileContent))
	elif userArgument == ("+t"):
		return(makeTabs(fileContent))
	elif (userArgument[:2] == "-T"):
		return(customSpacing(fileContent,userArgument[2:]))
	elif userArgument == ("+v"):
		return(makeVisable(fileContent))	
	elif userArgument == ("-v"):
		return(removeVisable(fileContent))
	else:
		return(fileContent)	#for no argument

def makeVisable(fileContent):
	'''
	MakeVisable is used to make all the required characters visable
	'''
	fileContent = fileContent.replace(chr(32),chr(183))
	fileContent = fileContent.replace(chr(9),chr(187)+chr(9))
	fileContent = fileContent+chr(182)
	return(fileContent)

def customSpacing(fileContent, spaceSize):
	'''
	Not exactly sure if this funcation is right. It takes the users -T(n) where n is an integer from and including 2-8
	and converts tabs to that length.
	'''
	if(not fileContent):
		pass
	else:
		spaceSize = int(spaceSize)
		customSpaceString = ''
		for i in range (0,spaceSize,1):
			customSpaceString += chr(32)
		posFirst = findFirstChr(fileContent)
		spaceString = ''
		spaceString = fileContent[:posFirst]
		spaceString = spaceString.replace(customSpaceString,chr(9))
		fileContent = spaceString + fileContent[posFirst:]
	return(fileContent)	

def findFirstChr(fileContent):
	'''
	Used to find the first non-space/tab in the fileContent string
	'''
	counter = 0
	found = False
	while found == False:
		a = fileContent[counter]
		posChr = ord(a)
		counter = counter + 1
		if (posChr != (32)) and (posChr != chr(9)):
			found = True
	return counter		

def makeTabs(fileContent):
	'''
	Used to make tabs out of spaces
	'''
	if(not fileContent):
		pass
	else:
		posFirst = findFirstChr(fileContent)
		spaceString = ''
		spaceString = fileContent[:posFirst]
		spaceString = spaceString.replace(chr(32)+chr(9),chr(9))
		spaceString = spaceString.replace(chr(32)+chr(32)+chr(9),chr(9))
		spaceString = spaceString.replace(chr(32)+chr(32)+chr(32)+chr(9),chr(9))
		spaceString = spaceString.replace(chr(32)+chr(32)+chr(32)+chr(32),chr(9))
		fileContent = spaceString + fileContent[posFirst:]
	return(fileContent)

def removeTabs(fileContent):
	'''
	Used to undo makeTabs (for normal -T4)
	'''
	if(not fileContent):
		pass
	else:
		posFirst = findFirstChr(fileContent)
		spaceString = ''
		spaceString = fileContent[:posFirst]
		spaceString = spaceString.replace(chr(9),chr(32)+chr(32)+chr(32)+chr(32))
		fileContent = spaceString + fileContent[posFirst:]
	return(fileContent)	

def removeVisable(fileContent):
	'''
	Removes Visable Characters
	'''
	fileContent = fileContent.replace(chr(183),chr(32))
	fileContent = fileContent.replace(chr(187)+chr(9),chr(9))
	fileContent = fileContent.strip(chr(182))
	return(fileContent)	##New Line end of file error

main() #On start								