#!/bin/bash
# Script to install homebrew, python3 and packages such as openpyxl to run the DataChecker.

# Install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# install python3 via homebrew
brew install python3
# install openpyxl via pip3
pip3 install openpyxl
