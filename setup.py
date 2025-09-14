from setuptools import setup, find_packages
from pathlib import Path

README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name="livedevsense",
    version="0.1.0",
    description="Sense, analyze, synthesize, and verify developer context and actions.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="LiveDevSense Contributors",
    url="https://example.com/livedevsense",
    license="MIT",
    python_requires=">=3.11",
    packages=find_packages(include=["livedevsense", "livedevsense.*", "analyzer", "sensors", "synthesizer", "verifier", "ui"]),
    include_package_data=True,
    install_requires=[
        "tesseract",
        "tree_sitter",
        "gitpython",
        "flask",
        "pytest",
        "watchdog",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)