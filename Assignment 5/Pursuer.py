import random

class Pursuer:
	'''
	Manages the Pursuer and the adjustment of percent to X's and Y's
	'''
	def __init__ (self):
		#Defaults
		self.xPercent = 50
		self.xCount = 0
		self.yCount = 0
	def setPercents(self, xPercent):
		self.xPercent = self.xPercent + xPercent #Changes the percent of X's up and down, this also changes the Y's, every non-X is a Y
	def runRandom(self):
		randomNum = random.randrange(1,101,1)
		if (randomNum <= self.xPercent):
			self.xCount = self.xCount + 1 #Add one for the count for post run stats
			return("x")
		else:
			self.yCount = self.yCount + 1
			return("y")	