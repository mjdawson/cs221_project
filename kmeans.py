import wav_manipulation as wm
import os
import random
import pickle
import collections

#key, time signature, tempo, valence, loudness, danceability, energy, acousticness, speechiness 

weights = [10., 10., 1., 1., 1., 1., 1., 1., 1.]
#ToDo: update to use new features
def calc_dist(feats1, feats2):

        # key: 0 to 12
        # time signature: int
        # tempo: BPM
        # valence: 0 to 1
        # loudness: -60 to 0
        # danceability: 0 to 1
        # energy: 0 to 1
        # acousticness: 0 to 1, confidence measure
        # speechiness: 0 to 1

        phi = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # if keys don't match, increase distance
	if feats1[0] != feats2[0]:
	    phi[0] = 1
	# if time signatures don't match, increase distance
	if feats1[1] != feats2[1]:
	    phi[1] = 1
        # tempo
        # percentage difference between 0 and 100
        phi[2] = abs(feats1[2] - feats2[2])/(100*max(feats1[2], feats2[2]))
        # valence
	phi[3] = abs(feats1[3] - feats2[3])

        # loudness
        phi[4] = abs(feats1[4] - feats2[4])

        #danceability
        phi[5] = abs(feats1[5] - feats2[5])

        #energy
        phi[6] = abs(feats1[6] - feats2[6])

        #acousticness
        phi[7] = abs(feats1[7] - feats2[7])

        #speechiness
        phi[8] = abs(feats1[8] - feats2[8])

        #dot product
        dist = 0
        for i in range(len(phi)):
            dist += phi[i]*weights[i]
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

def distTest(track_features):
    tracks = track_features.keys()
    distances = []
    for x in range(len(tracks)):
        for y in range(x+1, len(tracks)):
#            print "dist btwn %s and %s " % (tracks[x], tracks[y])
            dist = calc_dist(track_features[tracks[x]], track_features[tracks[y]])
            distances.append((tracks[x], tracks[y], dist))
 #           print dist
    sorted_dists = sorted(distances, key = lambda x: x[2], reverse = True)
    for dist in sorted_dists:
        print dist
if __name__ == "__main__":
	track_features = pickle.load(open('trackToFeatureTuples.p', 'rb'))
        distTest(track_features)

#	clusters = kmeans(track_features, 5)
#	for i in xrange(5):
#            print clusters[i]
	#	mashup_from_cluster(clusters[i], i)
