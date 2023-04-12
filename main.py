from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# YOUTUBE URL
yt = YouTube("...")
# Audio
stream = yt.streams.get_audio_only().download()
# Video
stream = yt.streams.get_highest_resolution().download()
