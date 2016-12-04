import ucs

class mashupSearchProblem(util.SearchProblem):
	def __init__(self, segs, maxNumSegs):
		self.segs = segs
		self.maxNumSegs = maxNumSegs

	def startState(self):
		return None

	def isEnd(self, state):
		return False

	def succAndCost(self, state):
		return None
	
