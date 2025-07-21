#!/usr/bin/env python3
"""
Hashing utilities for computing cryptographic hashes.
"""
import os
import hashlib

def compute_hashes(path, algorithm='sha256'):
    """Compute hashes for files in a directory or a single file."""
    hashes = {}
    if os.path.isfile(path):
        hashes[path] = hash_file(path, algorithm)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                try:
                    hashes[full_path] = hash_file(full_path, algorithm)
                except (PermissionError, FileNotFoundError) as e:
                    print(f"Skipped {full_path}: {e}")
    return hashes

def hash_file(file_path, algorithm='sha256'):
    """Compute the hash of a single file."""
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()