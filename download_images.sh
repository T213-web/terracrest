#!/bin/bash
# Download and optimize images for TerraCrest Group

echo "Downloading professional images from Unsplash..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Install it using: brew install python3 (macOS) or apt install python3 (Linux)"
    exit 1
fi

# Install required packages
echo "Installing required packages (requests, Pillow)..."
pip3 install requests Pillow --quiet

# Run the download script
python3 download_images.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Error occurred during download. Please check your internet connection."
    exit 1
fi

echo ""
echo "Success! Images have been downloaded and optimized."
