
class Segment():
	def __init__(self, trackName, featuresDict):
		self.trackName = trackName
		self.featuresDict = featuresDict
		self.visited = False

	def getLoudnessStart():
		return self.featuresDict["loudness_start"]

	def getLoudnessEnd():
		return self.featuresDict["loundess_end"]
	
	# returns pitches feature vector (as list)
	def getPitches():
		return self.featuresDict["pitches"]

	# returns timbre feature vector (as list)
	def getTimbre():
		return self.featuresDict["timbre"]
