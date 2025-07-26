#!/usr/bin/env python3
import json
import os #! unused 

from hasher import compute_hashes  # Import the compute_hashes function

def verify_hashes(saved_hash_file, root_dir):
    """Verify current file hashes against a saved hash database."""
    try:
        with open(saved_hash_file, 'r') as f:
            saved_hashes = json.load(f)
    except FileNotFoundError:
        print(f"Saved hash file {saved_hash_file} not found.")
        return {}

    current_hashes = compute_hashes(root_dir) # Compute current hashes 
    modified = []
    added = []
    deleted = []

# Compare current hashes with saved hashes
    for path, current_hash in current_hashes.items():
        if path not in saved_hashes:
            added.append(path)
        elif saved_hashes[path] != current_hash:
            modified.append(path)
            
    # Check for deleted files
    for path in saved_hashes:
        if path not in current_hashes:
            deleted.append(path)

    return {
        'modified': modified,
        'added': added,
        'deleted': deleted
    }