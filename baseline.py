import wav_manipulation as wm
import pickle
import random

track_features = pickle.load(open('trackToFeatureTuples.p', 'rb'))
tracks = track_features.keys()
random.shuffle(tracks)

tracks_to_use = tracks[:5]

random_segments = []
for i in xrange(5):
  start = 60 * random.random()
  end = start + 9
  segment = wm.cut_segment(tracks_to_use[i], start, end)
  random_segments.append(segment)

wm.stitch_segments(random_segments, 103)
