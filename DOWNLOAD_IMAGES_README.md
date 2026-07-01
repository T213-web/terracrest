# Download Images - TerraCrest Group Website

This folder contains scripts to download and optimize professional corporate images from Unsplash for your website.

## Quick Start

### Windows
1. Double-click **`download_images.bat`** 
2. The script will automatically download and optimize images
3. Images will be saved to the `images/` folder

### Mac / Linux
1. Open Terminal and navigate to this folder
2. Run: `bash download_images.sh`
3. Images will be saved to the `images/` folder

## Manual Setup (if scripts don't work)

### Requirements
- Python 3.7+
- pip (comes with Python)

### Installation
```bash
pip install requests Pillow
python download_images.py
```

## Images Being Downloaded

1. **hero-*.jpg** — Corporate team/office image (for hero section)
   - hero-800.jpg (800×450 for mobile)
   - hero-1600.jpg (1600×900 for desktop)
   - hero-3200.jpg (3200×1800 for retina displays)

2. **impact-*.jpg** — Business consulting/meeting image (for Our Impact section)
   - impact-800.jpg, impact-1600.jpg, impact-3200.jpg

3. **cta-*.jpg** — City skyline/finance image (for CTA section)
   - cta-800.jpg, cta-1600.jpg, cta-3200.jpg

All images are optimized for web (85% JPEG quality) to minimize file size while maintaining visual quality.

## What Happens After Download?

✓ Images are stored locally in `images/` folder
✓ Website will use local images instead of Unsplash (faster loading)
✓ Responsive <picture> tags serve optimized sizes by device
✓ 2x versions provided for retina/high-DPI displays

## Troubleshooting

**"Python is not found"**
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

**"requests or Pillow not found"**
- Run: `pip install requests Pillow`

**"Network timeout"**
- Check your internet connection
- Try again — Unsplash servers may be temporarily busy

## Questions?

If images fail to download, you can manually:
1. Visit Unsplash.com and search for: "corporate office team", "business meeting", "city skyline"
2. Download 1600×900 images
3. Rename to match filenames above
4. Save to `images/` folder
