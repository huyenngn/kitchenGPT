"""The kitchengpt package."""
from importlib import metadata

try:
    __version__ = metadata.version("kitchengpt")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0+unknown"
del metadata
