import wav_manipulation as wm
import os
import random
import pickle

#ToDo: update to use new features
def calc_dist(feats1, feats2):
	key1, time_sign1, tempo1 = feats1
	key2, time_sign2, tempo2 = feats2

	dist = 0

	if key1 != key2:
		dist += 50 
	
	if time_sign1 != time_sign2:
		dist += 70

	dist += abs(tempo1 - tempo2)
	return dist

def mashup_from_cluster(cluster, i):
	segments = []
	for track in cluster:
		segment_s = 20
		end_s = 30
		segment_title = wm.cut_segment(track, segment_s, end_s)
		if segment_title == None:
			continue
		segments.append(segment_title)

	wm.stitch_segments(segments, i)

#songs should be map from song index to (filename, audiofeatures)

#ToDo: update everything that needs track_features
def kmeans(track_features, k):
	max_iters = 1000

	tracks = track_features.keys()
	centroids = random.sample(tracks, k)
	clusters = [[] for i in xrange(k)]

	for i in xrange(max_iters):
		new_clusters = [[] for i in xrange(k)]

		for track in tracks:
			features = track_features[track]
			assigned_centroid = 0
			smallest_dist = float('inf')

			for j in xrange(k):
				centroid_features = track_features[centroids[j]]
				dist = calc_dist(features, centroid_features)
				if dist < smallest_dist:
					smallest_dist = dist
					assigned_centroid = j

			new_clusters[assigned_centroid].append(track)
		
		clusters = new_clusters

		for j in xrange(k):
			cluster = clusters[j]

			track_with_smallest_dist = -1
			smallest_dist = float('inf')

			for track in cluster:
				features = track_features[track]
				total_dist = 0

				for _track in cluster:
					_features = track_features[_track]
					total_dist += calc_dist(features, _features)

				if total_dist < smallest_dist:
					smallest_dist = total_dist
					track_with_smallest_dist = track
			
			centroids[j] = track_with_smallest_dist
	
	return clusters

if __name__ == "__main__":
        #change this
	track_features = pickle.load(open('trackToFeatures.p', 'rb'))
	clusters = kmeans(track_features, 5)
	for i in xrange(5):
		mashup_from_cluster(clusters[i], i)
