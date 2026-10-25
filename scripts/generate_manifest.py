from pathlib import Path
import json

root = Path(".")
assets = root / "assets"
extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".avif"}
files = sorted(
    f"assets/{path.name}"
    for path in assets.iterdir()
    if path.is_file() and path.suffix.lower() in extensions
)
(root / "images.json").write_text(
    json.dumps(files, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(f"Generated images.json with {len(files)} image(s).")
