import pickle
import kmeans as km
import jsonReadLib as j
from segment import Segment
from mashupSearchProblem import mashupSearchProblem
import segmentsCost as sc
import ucs
import random

track_features_small = pickle.load(open('trackToFeatureTuples.p', 'rb'))
clusters = km.kmeans(track_features_small, 5)

track_features_full = j.constructNamesToDict()

for cluster in clusters:
  # list of Segment objects
  cluster_segments = []
  for track in cluster:
    segments = track_features_full[track]["segments"]
    for i in xrange(len(segments)):
      s = Segment(track, i, segments[i])
      cluster_segments.append(s)

  start_segs = [s for s in cluster_segments if s.indexInTrack == 0]
  start = random.choice(start_segs)

  sp = mashupSearchProblem(cluster_segments, start, 20, sc.segmentsCost)
  ucs_alg = ucs.UniformCostSearch()
  ucs_alg.solve(sp)

  print [(a.trackName, a.indexInTrack) for a in ucs_alg.actions]
    
