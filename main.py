"""news-image-20261124 entry: sum up 24 November 2026 world news in one image.

The image (entry.jpg, 1024x1024) sits beside this program in the repository.
The program copies it to the output path and verifies the copy is exact and
within the 1 MiB limit. Deterministic: the same bytes on every run, no
network, no randomness.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1_048_576


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.jpg")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f_in, open(dst, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    if os.path.getsize(dst) > MAX_BYTES:
        raise SystemExit("output exceeds 1 MiB")
    if _sha256(src) != _sha256(dst):
        raise SystemExit("output differs from source image")


if __name__ == "__main__":
    main()
