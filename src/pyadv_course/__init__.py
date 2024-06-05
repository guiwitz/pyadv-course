"""Demo package for course."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-course")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Guillaume Witz"
__email__ = "guillaume.witz@unibe.ch"
