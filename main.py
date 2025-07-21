#!/usr/bin/env python3
"""
Main script for the Integrity Checker utility.
"""
import argparse
import json
import logging
import os
from datetime import datetime

# Import local modules
from hasher import compute_hashes, hash_file
from verifier import verify_hashes
from cli_parser import parse_args
from logger_setup import setup_logging, log_result

def save_hashes(hashes, output_file):
    """Save computed hashes to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(hashes, f, indent=4)
    logging.info(f"Hashes saved to {output_file}")

def main():
    args = parse_args()
    setup_logging()

    if args.command == 'hash':
        hashes = compute_hashes(args.path)
        save_hashes(hashes, args.output)
        print(f"Hashes saved to {args.output}")
    
    elif args.command == 'verify':
        result = verify_hashes(args.hashfile, args.dir)
        log_result(result)
        print("Verification Results:")
        for key, paths in result.items():
            if paths:
                print(f"{key.upper()}:")
                for path in paths:
                    print(f"  {path}")
    
    elif args.command == 'list':
        try:
            with open(args.hashfile, 'r') as f:
                hashes = json.load(f)
            print("Stored Hashes:")
            for path, hash_val in hashes.items():
                print(f"{path}: {hash_val}")
        except FileNotFoundError:
            print(f"Hash file {args.hashfile} not found.")
            logging.error(f"Hash file {args.hashfile} not found.")
    else:
        print("Invalid command. Use --help for usage.")

if __name__ == "__main__":
    main()