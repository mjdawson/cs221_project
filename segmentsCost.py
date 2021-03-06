dist_weights = [1., 3., 5.]

def l2NormWithDecay(v1, v2, gamma):
  assert len(v1) == len(v2)

  dist = 0.0
  for i in xrange(len(v1)):
    dist += ((v1[i] - v2[i]) ** 2) * (gamma ** i)

  return dist


def segmentsCost(seg1, seg2, numConsecSameSongSegs):
  #loudness_end1 = seg1.getLoudnessEnd()
  loudness_max1 = seg1[-1].getLoudnessMax()
  pitches1 = seg1[-1].getPitches()
  timbre1 = seg1[-1].getTimbre()

  #loudness_start2 = seg2.getLoudnessStart()
  loudness_max2 = seg2[0].getLoudnessMax()
  pitches2 = seg2[0].getPitches()
  timbre2 = seg2[0].getTimbre()

  #loudness_cost = abs(loundess_end1 - loudness_start2)
  loudness_cost = abs(loudness_max1 - loudness_max2)
  pitches_cost = l2NormWithDecay(pitches1, pitches2, 1)
  timbre_cost = l2NormWithDecay(timbre1, timbre2, 0.95)

#  baseline_threshold = 0
# threshold = baseline_threshold + 4 * numConsecSameSongSegs
  total_cost = dist_weights[0] * loudness_cost + dist_weights[1] * pitches_cost + dist_weights[2] * timbre_cost
  return total_cost

#  if total_cost < threshold or seg1.trackName != seg2.trackName:
#    return total_cost
#  else:
#    return threshold
  if numConsecSameSongSegs < 10 and seg1.trackName == seg2.trackName:
    return 0.0
  else:
    return total_cost


