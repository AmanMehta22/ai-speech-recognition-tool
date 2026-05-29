# pip install ffmpeg -y
# pip install -U yt-dlp

import yt_dlp

youtube_url = input("Enter YouTube URL: ")

# -----------------------------------
# High Quality Audio Extraction
# -----------------------------------
ydl_opts = {
    # Best available audio quality
    'format': 'bestaudio[ext=m4a]/bestaudio/best',

    # Output filename
    'outtmpl': 'audio.%(ext)s',

    # Ignore playlists
    'noplaylist': True,

    # Convert to WAV
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],

    # High quality ffmpeg settings
    'postprocessor_args': [
        '-ar', '16000',     # 16kHz sample rate
        '-ac', '1',         # mono channel
        '-vn',              # remove video
    ],

    'prefer_ffmpeg': True,

    # Better YouTube extraction reliability
    'extractor_args': {
        'youtube': {
            'player_client': ['android']
        }
    },

    # Quiet logs
    'quiet': False,
}

try:
    print("\nDownloading highest quality audio...\n")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    print("\nDone!")
    print("Saved as: audio.wav")

except Exception as e:
    print("\nDownload failed!")
    print("Error:", e)