#!/bin/bash

# Determine the directory where this .sh script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Script directory: $SCRIPT_DIR"

# Install Homebrew (package manager) if not already installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    echo "Homebrew installed."
else
    echo "Homebrew already installed."
fi

# Install Python
echo "Installing Python..."
brew install python

echo "Python installation complete."
python3 --version

# Upgrade pip
echo "Upgrading pip..."
pip3 install --upgrade pip

# Install PyInstaller
echo "Installing PyInstaller..."
pip3 install pyinstaller
echo "PyInstaller installed."

# Run pyinstall.py from the same folder as this script
echo "Running pyinstall.py..."
python3 "$SCRIPT_DIR/pyinstall.py"

echo "Done! Results should be inside a folder named dist as a .app "

