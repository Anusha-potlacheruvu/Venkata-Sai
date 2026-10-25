from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

SUPPORTED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"
}

def image_paths(folder, prefix):
    if not folder.exists():
        return []

    files = [
        path for path in folder.iterdir()
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
        and path.name.lower() != "logo.png"
    ]

    return [
        f"{prefix}/{path.name}"
        for path in sorted(files, key=lambda p: p.name.lower())
    ]

# Gold photos stay directly inside assets/.
gold_images = image_paths(ASSETS, "assets")

# Silver photos go inside assets/silver/.
silver_images = image_paths(ASSETS / "silver", "assets/silver")

(ROOT / "images.json").write_text(
    json.dumps(gold_images, indent=2) + "\n",
    encoding="utf-8"
)

(ROOT / "silver-images.json").write_text(
    json.dumps(silver_images, indent=2) + "\n",
    encoding="utf-8"
)

print(f"Generated {len(gold_images)} gold images")
print(f"Generated {len(silver_images)} silver images")
