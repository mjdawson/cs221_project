import pickle
import kmeans as km
import jsonReadLib as j
from segment import Segment
from mashupSearchProblem import mashupSearchProblem
import segmentsCost as sc
import ucs
import random
import wav_manipulation as wm

track_features_small = pickle.load(open('trackToFeatureTuples.p', 'rb'))
clusters = km.kmeans(track_features_small, 10)

track_features_full = j.constructNamesToDict()
cluster_num = 0

for cluster in clusters:
  # list of Segment objects
  cluster_30segments = []
  starts = []
  for track in cluster:
    segments = track_features_full[track]["segments"]

    segment30 = []
    for i in xrange(len(segments)):
      s = Segment(track, i, segments[i])
      segment30.append(s)
      if (i + 1) % 30 == 0:
        cluster_30segments.append(segment30)
        if i + 1 == 30:
          starts.append(segment30)
        segment30 = []

  start = random.choice(starts)

  sp = mashupSearchProblem(cluster_30segments, start, 5, sc.segmentsCost)
  ucs_alg = ucs.UniformCostSearch()
  ucs_alg.solve(sp)
  mashup = [s for s in start] + [s for a in ucs_alg.actions for s in a]
 
  segment_titles = []
  for seg in mashup:
    seg_start = seg.getStartTime()
    duration = seg.getDuration()
    seg_end = seg_start + duration

    title = wm.cut_segment(seg.trackName, seg_start, seg_end)
    if title == None:
      continue
    segment_titles.append(title)

  wm.stitch_segments(segment_titles, cluster_num)
  cluster_num += 1

  break

