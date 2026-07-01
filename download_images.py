#!/usr/bin/env python3
"""
Download and optimize professional corporate images from Unsplash for TerraCrest Group.
Requires: requests, Pillow (PIL)

Install dependencies:
  pip install requests Pillow
"""

import os
import requests
from PIL import Image
from io import BytesIO

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Image definitions: (url, output_filenames)
images = [
    {
        'name': 'Hero - Corporate Team',
        'url': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1600&h=900&fit=crop',  # corporate team in office
        'files': {
            'hero-800.jpg': (800, 450),
            'hero-1600.jpg': (1600, 900),
            'hero-3200.jpg': (3200, 1800),
        }
    },
    {
        'name': 'Impact - Business Consulting Meeting',
        'url': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1600&h=900&fit=crop',  # business team meeting
        'files': {
            'impact-800.jpg': (800, 450),
            'impact-1600.jpg': (1600, 900),
            'impact-3200.jpg': (3200, 1800),
        }
    },
    {
        'name': 'CTA - City Skyline / Finance',
        'url': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1600&h=900&fit=crop',  # city skyline/finance
        'files': {
            'cta-800.jpg': (800, 450),
            'cta-1600.jpg': (1600, 900),
            'cta-3200.jpg': (3200, 1800),
        }
    }
]

print('Downloading and optimizing images for TerraCrest Group...\n')

for img_set in images:
    print(f"Downloading: {img_set['name']}")
    try:
        # Download the image
        response = requests.get(img_set['url'], timeout=10)
        response.raise_for_status()
        
        # Open image
        img = Image.open(BytesIO(response.content))
        
        # Convert RGBA to RGB if needed
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (0, 0, 0))
            rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = rgb_img
        
        # Create resized versions
        for filename, (width, height) in img_set['files'].items():
            resized = img.resize((width, height), Image.Resampling.LANCZOS)
            output_path = os.path.join('images', filename)
            resized.save(output_path, 'JPEG', quality=85, optimize=True)
            file_size = os.path.getsize(output_path) / 1024
            print(f"  ✓ {filename} ({width}x{height}) - {file_size:.1f} KB")
        
        print()
    except Exception as e:
        print(f"  ✗ Error: {e}\n")

print("Done! All images downloaded and optimized in the 'images/' folder.")
print("\nThe website will now use these local images instead of Unsplash CDN.")
