import ucs

class mashupSearchProblem(util.SearchProblem):
	def __init__(self, segs, maxNumSegs, costFn):
		self.segs = segs
		self.maxNumSegs = maxNumSegs
		self.costFn = costFn

	# states are (last seg, # segs visited, # consecutive segs in same song)
	def startState(self):
		# randomly pick segment that has start position 0
		return (None, 0, 0)

	def isEnd(self, state):
		_, numSegsVisited, _ = state
		return numSegsVisited == self.maxNumSegs

	def succAndCost(self, state):
		lastSeg, numSegsVisited, numConsecSameSongSegs = state
		edges = []
		for seg in self.segs:
			# if seg visited, continue
			cost = self.costFn(seg, lastSeg, numConsecSameSongSegs)
			newNumSegsVisited = numSegsVisited + 1
			newNumConsecSameSongSegs = 0
			# if seg, lastSeg not from same song, increment newNumConsecSameSongs
			# new comment

			edges.append((seg, (seg, newNumSegsVisited, newNumConsecSameSongSegs), cost))
		
		return edges
		
	
