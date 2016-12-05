
def l2NormWithDecay(v1, v2, gamma):
	assert len(v1) == len(v2)

	dist = 0.0
	for i in xrange(len(v1)):
		dist += ((v1[i] - v2[i]) ** 2) * (gamma ** i)

	return dist


def segmentsCost(seg1, seg2, numConsecSameSongSegs):
	loudness_end1 = seg1.getLoudnessEnd()
	pitches1 = seg1.getPitches()
	timbre1 = seg1.getTimbre()

	loudness_start2 = seg2.getLoudnessStart()
	pitches2 = seg2.getPitches()
	timbre2 = seg2.getTimbre()

	loudness_cost = abs(loundess_end1 - loudness_start2)
	pitches_cost = l2NormWithDecay(pitches1, pitches2, 1)
	timbre_cost = l2NormWithDecay(timbre1, timbre2, 0.95)

	return loudness_cost + pitches_cost + timbre_cost


