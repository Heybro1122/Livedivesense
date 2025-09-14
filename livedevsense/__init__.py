"""LiveDevSense top-level package.

This package contains the core subpackages:
- livedevsense.sensors
- livedevsense.analyzer
- livedevsense.synthesizer
- livedevsense.verifier
- livedevsense.ui
"""

__version__ = "0.1.0"

# Expose subpackages under the livedevsense namespace.
from . import sensors, analyzer, synthesizer, verifier, ui  # noqa: F401

__all__ = ["sensors", "analyzer", "synthesizer", "verifier", "ui"]