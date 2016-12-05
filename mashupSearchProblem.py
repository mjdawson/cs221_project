import ucs

class mashupSearchProblem(ucs.SearchProblem):
  def __init__(self, seg30s, startSeg30, maxNumSegs, costFn):
    self.seg30s = seg30s
    self.startSeg = startSeg30[0]
    self.maxNumSegs = maxNumSegs
    self.costFn = costFn
    self.visited = {seg30[0] : False for seg30 in self.seg30s}
    self.segToSeg30 = {seg30[0] : seg30 for seg30 in self.seg30s}

  # states are (last seg, # segs visited, # consecutive segs in same song)
  def startState(self):
    return (self.startSeg, 0, 0)

  def isEnd(self, state):
    _, numSegsVisited, _ = state
    return numSegsVisited == self.maxNumSegs

  def succAndCost(self, state):
    print state
    lastSeg, numSegsVisited, numConsecSameSongSegs = state
    lastSeg30 = self.segToSeg30[lastSeg]
    self.visited[lastSeg] = True
    edges = []
    for seg30 in self.seg30s:
      if self.visited[seg30[0]]:
        continue

      # if segment is in same song but is not the next segment
      if seg30[0].trackName == lastSeg30[0].trackName and seg30[0].indexInTrack != lastSeg30[-1].indexInTrack + 1:
        continue

      cost = self.costFn(lastSeg30, seg30, numConsecSameSongSegs)
      newNumSegsVisited = numSegsVisited + 1
      newNumConsecSameSongSegs = 0
      if lastSeg30[0].trackName == seg30[0].trackName:
        newNumConsecSameSongSegs = numConsecSameSongSegs + 1

      edges.append((seg30, (seg30[0], newNumSegsVisited, newNumConsecSameSongSegs), cost))
    
    return edges
    
  
