# Integrity Checker (File Hashing Utility)
A Python-based tool to compute and verify cryptographic hashes (e.g., SHA-256, MD5) for files and directories, ensuring data integrity and detecting unauthorized modifications , which is a fundamental concept in operating systems and security..

## Description
This project implements a utility that calculates the cryptographic hash of files or directories. These hashes act as digital fingerprints. By storing these hashes and recalculating them later, the tool can verify if any files have been altered, added, or deleted. This is useful for checking the integrity of critical system files or detecting potential tampering.

## Features
- Compute SHA-256 or MD5 hashes for individual files or entire directories.
- Save computed hashes to a JSON database file.
- Verify the integrity of files/directories by comparing current hashes against the saved database.
- Detect modified, added, and deleted files.
- Log actions and results to a file for auditing.
- (Optional) Sign the hash database for added security (using `cryptography`).

## Requirements
- **Operating System**: Linux (Ubuntu/Debian recommended), macOS, or Windows Subsystem for Linux (WSL).
- **Python**: Python 3.6 or higher.
- **Internet Access**: To download Python packages.
- **Optional**: `cryptography` library for signing the hash database.

## Installation & Setup (Linux/WSL)
Follow these steps to set up and run the project from scratch.

- if u have account u should only write at the terminal --> **wsl**
- if u don't have account u should write at the terminal --> **wsl --install**
- if u want to uninstall --> **wsl --unregister Ubuntu**

### 1. Install dependencies:
Open a terminal and run:
```bash
sudo apt update && sudo apt upgrade -y
```
   ```bash
   pip install -r requirements.txt
   ```

#### 1. Compute hashes:
   ```bash
   python main.py hash --path /etc --output hashes.json
   ```
#### 2. Verify hashes:
```bash
   python main.py verify --hashfile hashes.json --dir /etc
```
#### 3. List stored hashes:
```bash
   python main.py list --hashfile hashes.json
```
### 2. Install Python and Virtual Environment Tools
```bash
sudo apt install python3 python3-venv python3-pip -y
```   
### 3. Create a Project Directory
```bash
cd ~
mkdir integrity_checker_project
cd integrity_checker_project
```   
### 4. Create Project Files (You need to create the following Python files in your project directory (~/integrity_checker_project))
- do it for each file u have it at the project directory "
```bash
nano main.py
nano hasher.py
nano verifier.py
nano cli_parser.py
nano logger_setup.py
nano security_utils.py
nano requirements.txt
nano README.md
nano test_integrity_checker.py 
nano integrity_checker.log 
nano hashes.json
```
-then save and exit (Ctrl+O, Enter, Ctrl+X)

### 5. Set Up a Virtual Environment
```bash
# Create the virtual environment (without pip initially)
python3 -m venv venv --without-pip

# Activate the virtual environment
source venv/bin/activate
```

### 6. Install pip and Dependencies
```bash
# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip
python get-pip.py

# Install project dependencies
pip install -r requirements.txt
pip install cryptography
```

## Running the tool : ensure at directory (~/integrity_checker_project) + venv activated

### 1. Create a Test Directory and File
```bash
mkdir test_dir
echo "original test content" > test_dir/test_file.txt
```

### 2. Compute Hashes  
```bash
python main.py hash --path test_dir --output hashes.json
```

### 3. Verify Hashes (No Changes)
```bash
python main.py verify --hashfile hashes.json --dir test_dir
```

### 4. Modify a File nad Verify Again
```bash
echo "modified test content" > test_dir/test_file.txt
python main.py verify --hashfile hashes.json --dir test_dir
```

### 5. List Stored Hashes
```bash
python main.py list --hashfile hashes.json
```

### 6. check the Log file 
```bash
cat integrity_checker.log
```
## done by:
- Maryam Ali Hasan 202209427
- Nada Abdulaziz 202203864
- Noora abdulatif 202308545


ls -la ~/
ls -la

cd /home/maryamali/integrity_checker_project
cd /mnt/c/Users/meeme/Integrity-Checker-
