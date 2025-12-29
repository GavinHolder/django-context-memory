"""
Django Context Memory - Deep code intelligence for AI assistants

A standalone library for generating structured, machine-readable context
from Django codebases to improve AI assistant performance.
"""

__version__ = "1.0.0"
__author__ = "Gavin Holder"
__license__ = "MIT"

from .analyzer import CodeAnalyzer
from .builder import ContextBuilder
from .scanner import ProjectScanner
from .config import Config
from . import utils

__all__ = [
    "CodeAnalyzer",
    "ContextBuilder",
    "ProjectScanner",
    "Config",
    "utils",
]
