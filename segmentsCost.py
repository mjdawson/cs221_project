
def l2NormWithDecay(v1, v2, gamma):
  assert len(v1) == len(v2)

  dist = 0.0
  for i in xrange(len(v1)):
    dist += ((v1[i] - v2[i]) ** 2) * (gamma ** i)

  return dist


def segmentsCost(seg1, seg2, numConsecSameSongSegs):
  #loudness_end1 = seg1.getLoudnessEnd()
  loudness_max1 = seg1.getLoudnessMax()
  pitches1 = seg1.getPitches()
  timbre1 = seg1.getTimbre()

  #loudness_start2 = seg2.getLoudnessStart()
  loudness_max2 = seg2.getLoudnessMax()
  pitches2 = seg2.getPitches()
  timbre2 = seg2.getTimbre()

  #loudness_cost = abs(loundess_end1 - loudness_start2)
  loudness_cost = abs(loudness_max1 - loudness_max2)
  pitches_cost = l2NormWithDecay(pitches1, pitches2, 1)
  timbre_cost = l2NormWithDecay(timbre1, timbre2, 0.95)

  baseline_threshold = 0
  threshold = baseline_threshold + 4 * numConsecSameSongSegs
  total_cost = loudness_cost + pitches_cost + timbre_cost

  if total_cost < threshold or seg1.trackName != seg2.trackName:
    return total_cost
  else:
    return threshold


