# Venkata Sai Gold & Silvers — Image Gallery

A simple static website that displays image files from `assets/`. The GitHub Actions workflow automatically rebuilds `images.json` whenever you push to the `main` branch.

## Folder structure

```text
venkata-sai-image-gallery/
├── index.html
├── images.json                 # Generated automatically during deployment
├── assets/                     # Put your images here
│   ├── diwali-banner.png
│   ├── logo-transparent.png
│   └── product-photo.jpg
├── scripts/
│   └── generate_manifest.py
└── .github/
    └── workflows/
        └── pages.yml
```

## Publish on GitHub Pages

1. Create a GitHub repository, for example `venkata-sai-gallery`.
2. Upload the contents of this folder to the repository's `main` branch.
3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment → Source**, select **GitHub Actions**.
5. Open the **Actions** tab and wait for “Build and deploy image gallery” to finish successfully.
6. Open **Settings → Pages** to find the published website URL.

## Add more images later

Copy `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.svg`, or `.avif` files into `assets/`, then commit and push them to `main`. The workflow automatically updates the image list and republishes the gallery.

## Read-only for visitors

For a public gallery, make the repository **Public**. Anyone can view the website and repository, but only you (the owner) and people you explicitly grant write access can change the files. Do not add other people as collaborators with write access. Public visitors can still save or copy images, so this is view-only for editing—not copy-protection.

If the repository is private, public visitors generally cannot view the website; availability of private GitHub Pages depends on your GitHub plan and organization settings.
