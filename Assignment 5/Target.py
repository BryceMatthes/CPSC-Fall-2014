import random

class Target:
	'''
	Manages the target in the date.
	'''
	def __init__ (self):
		#Defaults
		self.xPercent = 0
		self.xCount = 0
		self.yCount = 0
	def setPercents(self, xPercent):
		#Sets the percent value of X's in the simulation
		self.xPercent = xPercent
	def runRandom(self):
		randomNum = random.randrange(1,101,1)
		if (randomNum <= self.xPercent):
			self.xCount = self.xCount + 1 #Add one for the count for post run stats
			return("x")
		else:
			self.yCount = self.yCount + 1
			return("y")