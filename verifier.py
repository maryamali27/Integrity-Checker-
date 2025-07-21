#!/usr/bin/env python3
"""
Hash verification utilities.
"""
import json
import os
from hasher import compute_hashes

def verify_hashes(saved_hash_file, root_dir):
    """Verify current file hashes against a saved hash database."""
    try:
        with open(saved_hash_file, 'r') as f:
            saved_hashes = json.load(f)
    except FileNotFoundError:
        print(f"Saved hash file {saved_hash_file} not found.")
        return {}

    current_hashes = compute_hashes(root_dir)
    modified = []
    added = []
    deleted = []

    for path, current_hash in current_hashes.items():
        if path not in saved_hashes:
            added.append(path)
        elif saved_hashes[path] != current_hash:
            modified.append(path)
    
    for path in saved_hashes:
        if path not in current_hashes:
            deleted.append(path)

    return {
        'modified': modified,
        'added': added,
        'deleted': deleted
    }