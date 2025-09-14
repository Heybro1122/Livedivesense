# Livedivesense

## OCR Sensor (Ticket 2)

This repository includes an OCR sensor that uses Tesseract (via `pytesseract`) to extract text from images.

### Installation

1) Install the Tesseract binary on your system:

- macOS (Homebrew):
  - `brew install tesseract`
- Ubuntu/Debian:
  - `sudo apt-get update && sudo apt-get install -y tesseract-ocr`
- Windows:
  - Install from https://github.com/UB-Mannheim/tesseract/wiki
  - Ensure the Tesseract installation directory is added to your PATH.

2) Install Python dependencies (Python 3.11):

- Using pip:
  - `pip install pillow pytesseract`
- Or with a requirements file (if used in your environment):
  - `pip install -r requirements.txt`

### Usage

```python
from sensors.ocr_sensor import extract_text

text = extract_text("path/to/image.png")
print(text)
```

The function raises a RuntimeError with guidance if Tesseract or required Python packages are not available.

### Running the test

The test dynamically generates a sample image and performs OCR. It will skip automatically if Tesseract or the required Python packages are not available in the environment.

```bash
pytest -k test_ocr_sensor
```