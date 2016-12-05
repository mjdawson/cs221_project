import ucs

class mashupSearchProblem(util.SearchProblem):
	def __init__(self, segs, maxNumSegs, costFn):
		self.segs = segs
		self.maxNumSegs = maxNumSegs
		self.costFn = costFn

	def startState(self):
		return ([], 0)

	def isEnd(self, state):
		visitedSegs, numInSameSong = state
		return len(visitedSegs) == self.maxNumSegs

	def succAndCost(self, state):
		visitedSegs, numInSameSong = state
		edges = []
		
		
		return edges
		
	
