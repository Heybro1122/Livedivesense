"""LiveDevSense top-level package.

This package ties together the core subpackages:
- sensors
- analyzer
- synthesizer
- verifier
- ui

The subpackages currently live at the repository top-level (e.g., `sensors`, `analyzer`).
To offer a stable import path, we expose them under the `livedevsense` namespace as well:
`from livedevsense import sensors, analyzer, synthesizer, verifier, ui`.
"""

from importlib import import_module

__version__ = "0.1.0"

# Re-export top-level packages under this namespace for convenience.
sensors = import_module("sensors")
analyzer = import_module("analyzer")
synthesizer = import_module("synthesizer")
verifier = import_module("verifier")
ui = import_module("ui")

__all__ = ["sensors", "analyzer", "synthesizer", "verifier", "ui"]