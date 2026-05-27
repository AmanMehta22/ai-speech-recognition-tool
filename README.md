# AI Speech Recognition Tool

A compact, notebook-first demo that downloads audio (via `yt-dlp`) from a YouTube URL and transcribes it with OpenAI Whisper. This repository contains a working demo, a helper script to extract audio, and notes for running and extending the pipeline.

Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Usage](#usage)
	- [Command-line audio extraction](#command-line-audio-extraction)
	- [Notebook transcription demo](#notebook-transcription-demo)
- [Output & Artifacts](#output--artifacts)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Development & Next Steps](#development--next-steps)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates an end-to-end speech-to-text flow:

1. Download audio from a YouTube URL using `yt-dlp`.
2. (Optional) Use a GPU (CUDA) if available for faster transcription.
3. Transcribe audio using OpenAI Whisper (recommended: `large-v3`).
4. Save the transcript to `audio.txt`.

## Features

- Easy demo via Jupyter notebook
- Simple CLI helper to extract audio (`extract_audio.py`)
- GPU-aware transcription using PyTorch/Whisper
- Clear outputs suitable for demos or prototyping

## Requirements

- Python 3.10+
- ffmpeg (required by `yt-dlp` and Whisper for many media formats)
- Internet access (for model and media downloads)
- Optional: NVIDIA GPU with CUDA for faster transcription

Install system dependencies (example, Ubuntu):

```bash
sudo apt update
sudo apt install -y ffmpeg python3-venv
```

## Quick Start

1. Create and activate a virtual environment:

```powershell
# Windows (PowerShell)
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

```bash
# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Extract audio from a YouTube URL (see next section) and then run the notebook demo to transcribe.

## Usage

### Command-line audio extraction

This repo includes a small helper script to download the best audio stream from a YouTube URL. Run it and provide the URL when prompted.

```powershell
python extract_audio.py
# Enter a URL when prompted; the script writes audio.<ext> (e.g., audio.m4a)
```

`extract_audio.py` tries two extraction methods (normal and an Android fallback). If both fail, check the stderr for yt-dlp errors.

### Notebook transcription demo

Open the provided notebook in Jupyter or VS Code (e.g., `stt.ipynb` or `work.ipynb` if present) and run cells in order. Typical steps in the notebook:

- Verify PyTorch device / CUDA availability.
- Load the Whisper model: `whisper.load_model("large-v3")` (or choose a smaller model for lower memory usage).
- Run `model.transcribe("audio.<ext>")` and write `result["text"]` to `audio.txt`.

Example Python snippet (from a notebook or script):

```python
import whisper

model = whisper.load_model("large-v3")
res = model.transcribe("audio.m4a")
print(res["text"])
with open("audio.txt", "w", encoding="utf-8") as f:
		f.write(res["text"])
```

Notes:
- For low-memory environments, use a smaller Whisper model (e.g., `small`, `base`).
- First-run model loads may download model files and take time.

## Output & Artifacts

- `audio.<ext>` — downloaded audio file created by `extract_audio.py` or `yt-dlp` in the notebook
- `audio.txt` — transcription output (UTF-8 plain text)

## Troubleshooting

- yt-dlp fails: ensure `ffmpeg` is installed and the URL is valid.
- Whisper out-of-memory on GPU: switch to CPU or use a smaller model.
- Slow transcription: ensure GPU drivers and CUDA are installed and correctly configured.

## Project Structure

```
.
|-- extract_audio.py      # helper script to download audio from YouTube
|-- stt.ipynb             # notebook demo (may be named work.ipynb in older versions)
|-- REPORT.md             # short project report and recommendations
|-- DEMO_CHECKLIST.md     # demo checklist and talking points
|-- requirements.txt      # Python dependencies
|-- audio.txt             # sample transcription output (optional)
`-- README.md
```

## Development & Next Steps

Recommended improvements for production or reproducible demos:

- Add `transcribe.py` CLI to run transcription outside the notebook.
- Add tests and CI checks for environment and small smoke tests.
- Provide a `Dockerfile` (or `docker-compose`) with optional GPU passthrough for repeatable demos.
- Modularize the pipeline (download → preprocess → transcribe → postprocess).

## Contributing

Contributions are welcome. Open an issue or a pull request describing the change.

## License

This project does not include a license file. Add a `LICENSE` if you want to make the code open-source. For internal demos, follow your organization's policy.

---

If you'd like, I can:
- add a `transcribe.py` CLI wrapper that uses the same notebook logic,
- create a `requirements.txt` if it's missing or pin versions,
- or convert the notebook into runnable scripts and add a `Dockerfile`.

