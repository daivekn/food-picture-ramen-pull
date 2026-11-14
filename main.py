"""Write the entry image: a steaming tonkotsu ramen noodle lift."""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ramen-noodle-pull.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(OUT_DIR, exist_ok=True)
with open(SRC, "rb") as src, open(os.path.join(OUT_DIR, "entry.png"), "wb") as dst:
    shutil.copyfileobj(src, dst, length=1024 * 1024)
