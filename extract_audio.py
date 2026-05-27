import yt_dlp

youtube_url = input("Enter YouTube URL: ")

# -------------------------------
# Method 1 : Normal extraction
# -------------------------------
method1_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
}

# -------------------------------
# Method 2 : Android fallback
# -------------------------------
method2_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'extractor_args': {
        'youtube': {
            'player_client': ['android']
        }
    }
}

try:
    print("\nTrying Method 1 (Normal Extraction)...\n")

    with yt_dlp.YoutubeDL(method1_opts) as ydl:
        ydl.download([youtube_url])

    print("\nAudio downloaded successfully using Method 1!")

except Exception as e:

    print("\nMethod 1 failed!")
    print("Error:", e)

    print("\nTrying Method 2 (Android Fallback)...\n")

    try:
        with yt_dlp.YoutubeDL(method2_opts) as ydl:
            ydl.download([youtube_url])

        print("\nAudio downloaded successfully using Method 2!")

    except Exception as e2:

        print("\nMethod 2 also failed!")
        print("Error:", e2)

        print("\nCould not extract audio from this URL.")