# Demo Checklist

1. Environment
   - Activate virtual environment and install `requirements.txt`.

2. Verify GPU (optional)
   - In the first cell of `work.ipynb`, run the CUDA checks to show GPU availability.

3. Run demo
   - Execute the YouTube download cell and confirm `audio.*` is created.
   - Execute the transcription cell; wait for model to finish.
   - Open `audio.txt` to show transcript output.

4. Talking points
   - Explain choice of tools (`yt-dlp`, Whisper).
   - Mention GPU vs CPU performance and memory requirements.
   - Describe challenges and next improvements (modular scripts, tests, Docker).
