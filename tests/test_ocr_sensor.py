import os
import sys
from pathlib import Path

import pytest

# Ensure the package root is importable when running tests directly
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sensors.ocr_sensor import extract_text


@pytest.mark.skipif(
    os.environ.get("CI", "") == "true",
    reason="Skip OCR test in CI environments without Tesseract",
)
def test_extract_text_on_sample_image(tmp_path: Path):
    """
    This test uses a dynamically generated image to avoid committing binary assets.
    It requires local Tesseract installation and Pillow.
    """
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception as e:
        pytest.skip(f"Pillow not available: {e}")

    # Try to import pytesseract and check tesseract availability
    try:
        import pytesseract
        pytesseract.get_tesseract_version()
    except Exception as e:
        pytest.skip(f"Tesseract not available: {e}")

    # Create a simple image with clear text
    img = Image.new("RGB", (400, 120), color="white")
    draw = ImageDraw.Draw(img)
    # Use a default font; not all environments have a TTF available
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 36)
    except Exception:
        font = ImageFont.load_default()

    sample_text = "Hello OCR"
    draw.text((10, 40), sample_text, fill="black", font=font)

    img_path = tmp_path / "sample.png"
    img.save(img_path)

    text = extract_text(str(img_path))
    # Normalize whitespace and case for robustness
    normalized = " ".join(text.split()).strip().lower()
    assert "hello" in normalized and "ocr" in normalized