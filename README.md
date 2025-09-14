# LiveDevSense

LiveDevSense is a zero-cost, open-source toolkit that senses developer activity, analyzes intent and code state, synthesizes helpful next steps, and verifies results — all with a simple, extensible architecture.

It is organized into five logical components:
- sensors: Collect signals (filesystem events, git activity, editor/UI hooks, OCR capture, etc.)
- analyzer: Turn raw signals and code artifacts into structured context using parsing and heuristics
- synthesizer: Propose actions (patches, commands, prompts) based on the analyzed context
- verifier: Validate proposed actions by running checks/tests and confirming outcomes
- ui: Provide a developer-facing interface (e.g., Flask web UI) to visualize and control the system

## Requirements

- Python 3.11+
- Optional system dependency for OCR sensors:
  - Tesseract OCR engine (binary) may be required for OCR-based sensors  
    - macOS: `brew install tesseract`  
    - Ubuntu/Debian: `sudo apt-get install tesseract-ocr`

Python dependencies are listed in requirements.txt and kept open-source and zero-cost.

## Quickstart

1) Create and activate a virtual environment
- macOS/Linux:
  - `python3.11 -m venv .venv && source .venv/bin/activate`
- Windows:
  - `py -3.11 -m venv .venv && .venv\Scripts\activate`

2) Install dependencies and the package in editable mode
- `pip install -r requirements.txt`
- `pip install -e .`

3) Run tests (if/when added)
- `pytest -q`

4) Run the UI (placeholder)
- A Flask-based dev UI can live under the `ui` package. Example app scaffolding can be added in a later ticket.

## Project Layout

- analyzer/   — process events and code to derive intent and context
- sensors/    — collect signals from the environment (FS, git, OCR, etc.)
- synthesizer/— propose next actions or code changes
- verifier/   — verify actions via checks and tests
- ui/         — developer-facing interface (e.g., Flask)

Each directory is a Python package to keep the code modular and testable.

## Contributing

- Keep the code Python 3.11 compatible.
- Prefer simple, composable modules with clear responsibilities.
- Add tests with pytest where relevant.

## License

Open-source and zero-cost. License to be added in a future ticket if needed.