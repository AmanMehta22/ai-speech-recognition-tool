# Project Report — AI Speech Recognition Tool

Objective
- Build an end-to-end demo that downloads audio from YouTube and produces text transcripts using Whisper.

Approach
- Audio extraction: `yt-dlp` to obtain best audio stream.
- Transcription: OpenAI Whisper model called from the notebook; output written to `audio.txt`.

Results
- Notebook `work.ipynb` demonstrates the full flow; transcript is saved as `audio.txt` in the repo root.

Challenges
- Dependency/version sensitivity (GPU drivers, PyTorch/whisper versions).
- Notebook-only workflow reduces reusability; consider script modularization for production.

Next steps (recommended but not applied here)
- Add small CLI scripts (`download.py`, `transcribe.py`) and unit/smoke tests.
- Provide a Dockerfile for reproducible GPU/non-GPU runs.

Deliverables for internship submission
- `work.ipynb` (notebook demo)
- `audio.txt` (sample transcript)
- Short report (this file) and a 2–5 minute demo video showing the pipeline.
