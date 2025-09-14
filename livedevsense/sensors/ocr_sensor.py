from __future__ import annotations
from PIL import Imageimport pytesseract
from pytesseract import TesseractNotFoundError
def _ensure_tesseract_available() -> None:
    """    Ensure the Tesseract OCR binary is available on the system.
    Raises:
        RuntimeError: If the Tesseract binary cannot be found.    """
    try:        # Triggers discovery of the tesseract binary and raises if missing
        pytesseract.get_tesseract_version()    except TesseractNotFoundError as e:
        raise RuntimeError(            "Tesseract OCR engine is not installed or not found on PATH. "
            "Install it (e.g., `sudo apt-get install tesseract-ocr`, "            "`brew install tesseract`, or see https://tesseract-ocr.github.io/) "
            "and ensure the `tesseract` binary is available."        ) from e

def extract_text(image_path: str) -> str:    """
    Extract text from an image using Tesseract via pytesseract.
    Args:        image_path: Path to the image file.
    Returns:
        The extracted text.
    Raises:        FileNotFoundError: If the image file does not exist.
        RuntimeError: If the Tesseract binary is missing.    """
    _ensure_tesseract_available()
    # Open and normalize the image    with Image.open(image_path) as img:
        # Convert to a common mode to avoid issues with paletted images        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")        text = pytesseract