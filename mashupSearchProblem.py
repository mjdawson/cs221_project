import ucs

class mashupSearchProblem(ucs.SearchProblem):
  def __init__(self, segs, startSeg, maxNumSegs, costFn):
    self.segs = segs
    self.startSeg = startSeg
    self.maxNumSegs = maxNumSegs
    self.costFn = costFn
    self.visited = {seg : False for seg in self.segs}

  # states are (last seg, # segs visited, # consecutive segs in same song)
  def startState(self):
    return (self.startSeg, 0, 0)

  def isEnd(self, state):
    _, numSegsVisited, _ = state
    return numSegsVisited == self.maxNumSegs

  def succAndCost(self, state):
    lastSeg, numSegsVisited, numConsecSameSongSegs = state
    self.visited[lastSeg] = True
    edges = []
    for seg in self.segs:
      if self.visited[seg]:
        continue

      # if segment is in same song but is not the next segment
      if seg.trackName == lastSeg.trackName and seg.indexInTrack != lastSeg.indexInTrack + 1:
        continue

      cost = self.costFn(seg, lastSeg, numConsecSameSongSegs)
      newNumSegsVisited = numSegsVisited + 1
      newNumConsecSameSongSegs = 0
      if lastSeg.trackName == seg.trackName:
        newNumConsecSameSongSegs = numConsecSameSongSegs + 1

      edges.append((seg, (seg, newNumSegsVisited, newNumConsecSameSongSegs), cost))
    
    return edges
    
  
