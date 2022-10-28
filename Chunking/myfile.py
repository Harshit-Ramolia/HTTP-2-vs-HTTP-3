from ffmpeg_streaming import Formats, input
from os import startfile, path
print(path.abspath('testfiles/test.mp4'))
# startfile(path.abspath('testfiles/test.mp4'))
video = input(path.abspath('testfiles/test.mp4'))
dash = video.dash(Formats.h264())
# print(dash)
from ffmpeg_streaming import Bitrate, Representation, Size

# _144p  = Representation(Size(256, 144), Bitrate(95 * 1024, 64 * 1024))
# dash.representations(_144p)# _720p, _1080p, _2k, _4k)

dash.auto_generate_representations()
# dash.generate_hls_playlist()
dash.output(path.abspath('testfiles/x.mpd'))
# print(video)
