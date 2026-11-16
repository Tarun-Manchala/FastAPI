import uuid  # generated unique file names
from io import BytesIO  # works with image bits and memory
from pathlib import Path  # file operations

from PIL import Image, ImageOps

PROFILE_PICS_DIR = Path("media/profile_pics")
