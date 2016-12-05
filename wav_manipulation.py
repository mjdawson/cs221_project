import wave
import os.path

DIR = "./songs_wav/"

def cut_segment(trackname, start_s, end_s):
  # might need to deal with directories
  filename = DIR + trackname + '.wav'
  if not os.path.isfile(filename):
    return None
  wr = wave.open(filename, 'rb')

  num_chan = wr.getnchannels()
  sample_width = wr.getsampwidth()

 

  num_frames = wr.getnframes()
  frame_rate = wr.getframerate()
  
  front = int(frame_rate * start_s)
  front_f = wr.readframes(front)
  middle = int(frame_rate * (end_s - start_s))
  middle_f = wr.readframes(middle)

  #segment_frames = frames[int(start_s * frame_rate) : int(end_s * frame_rate)]
  
  segment_title = trackname + ':' + str(start_s) + '-' + str(end_s)
  segment_filename = segment_title + '.wav'

  ww = wave.open(segment_filename, 'wb')
  ww.setnchannels(num_chan)
  ww.setsampwidth(sample_width)
  ww.setframerate(frame_rate)
  ww.writeframes(middle_f)

  wr.close()
  ww.close()

  return segment_title

def stitch_segments(segments, cluster_num):
  if len(segments) == 0:
    return

  first_filename = segments[0] + '.wav'
  wr = wave.open(first_filename, 'rb')

  # use these values from first file for new file
  num_chan = wr.getnchannels()
  sample_width = wr.getsampwidth()
  frame_rate = wr.getframerate()

  wr.close()

  frames = None

  for trackname in segments:
    filename = trackname + '.wav'
    wr = wave.open(filename, 'rb')
    num_frames = wr.getnframes()
    
    if frames == None:
      frames = wr.readframes(num_frames)
    else:
      frames += wr.readframes(num_frames)
    wr.close()

  if frames == None:
    return
  #mashup_filename = ''
  #for trackname in segments:
  # mashup_filename += trackname
  
  mashup_filename = 'cluster_' + str(cluster_num) + '.wav'

  ww = wave.open(mashup_filename, 'wb')
  ww.setnchannels(num_chan)
  ww.setsampwidth(sample_width)
  ww.setframerate(frame_rate)
  ww.writeframes(frames)

  ww.close()



