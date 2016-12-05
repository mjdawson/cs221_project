
class Segment():
  def __init__(self, trackName, indexInTrack, featuresDict):
    self.trackName = trackName
    self.indexInTrack = indexInTrack
    self.featuresDict = featuresDict
    self.visited = False

  def getLoudnessStart(self):
    return self.featuresDict["loudness_start"]

  def getLoudnessEnd(self):
    return self.featuresDict["loudness_end"]

  def getLoudnessMax(self):
    return self.featuresDict["loudness_max"]
  
  # returns pitches feature vector (as list)
  def getPitches(self):
    return self.featuresDict["pitches"]

  # returns timbre feature vector (as list)
  def getTimbre(self):
    return self.featuresDict["timbre"]
  
  def getStartTime(self):
    return self.featuresDict["start"]
  
  def getDuration(self):
    return self.featuresDict["duration"]
