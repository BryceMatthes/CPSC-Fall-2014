# Your name: Bryce Matthes  
# Student ID: 10147880
# Tutorial #: T07
# Version: 1.0
# LC: 64

'''
Mini assignment 6, last one of 231.

Uses two classes Cat and Dog to manage name and age
of each animal. 
'''

class Cat:
	'''
	This class is used to handle the name
	and age of an instance of Cat
	'''
	def __init__ (self):
		#Default name and age
		self.name = "no name"
		self.age = -1
	def getName(self):
		#returns name.
		return self.name
	def getAge(self):
		#returns age
		return self.age
	def setName(self, name):
		#Sets name to the argument (name)
		self.name = name
	def setAge(self, age):
		#Sets age to the argument (age)
		self.age = age
	def makeSound(self):
		#You still need self for this to work.
		print("meow")

class Dog:
	'''
	See Cat class for documentation.
	'''
	def __init__ (self):
		self.name = "no name"
		self.age = -1
	def getName(self):
		return self.name
	def getAge(self):
		return self.age
	def setName(self, name):
		self.name = name
	def setAge(self, age):
		self.age = age
	def makeSound(self):
		print("bark")

def main(): #main function
	'''
	Used to display data from the two classes Dog and Cat
	'''
	dogCall = Dog()
	catCall = Cat()
	print("Dog Name: "+dogCall.name+", Dog Age: "+str(dogCall.age)) #Displays dog defaults
	print("Cat Name: "+catCall.name+", Cat Age: "+str(catCall.age)) #Displays dog defaults
	catCall.setAge(7) #Set cat age to 7
	catCall.setName("Tigger") #Set cat name to 'Tigger'
	print("Cat Name: "+catCall.name+", Cat Age: "+str(catCall.age)) #Displays updated cat name and age.



main()														