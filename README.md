# Integrity Checker (File Hashing Utility)

## Description
A Python-based tool to compute and verify cryptographic hashes (e.g., SHA-256, MD5) for files and directories, ensuring data integrity and detecting unauthorized modifications.

## Features
- Compute hashes for single files or directories.
- Verify hashes against a saved database.
- Detect modified, added, or deleted files.
- Logging for audit trails.

## Requirements
- Python 3.x
- `cryptography` library (for optional signing)

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt


   # run these commands in the terminal
   1. Compute hashes:
   python main.py hash --path /etc --output hashes.json

   2. Verify hashes:
   python main.py verify --hashfile hashes.json --dir /etc

   3. List stored hashes:
   python main.py list --hashfile hashes.json


#To install the required dependencies, try one of the following:
1. Use python -m pip (most reliable on Windows):
python -m pip install -r requirements.txt

2. 2. If you have Python 3 specifically, try:
python3 -m pip install -r requirements.txt

##done by:
- Maryam Ali Hasan 202209427
-
-
