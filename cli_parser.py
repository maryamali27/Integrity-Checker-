#!/usr/bin/env python3
"""
Command-line argument parser.
"""
import argparse

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    subparsers = parser.add_subparsers(dest='command')

    # Hash command
    hash_parser = subparsers.add_parser('hash', help='Compute hashes')
    hash_parser.add_argument('--path', required=True, help='File or directory to hash')
    hash_parser.add_argument('--output', required=True, help='Output JSON file')
    hash_parser.add_argument('--algorithm', default='sha256', choices=['sha256', 'md5'])

    # Verify command
    verify_parser = subparsers.add_parser('verify', help='Verify hashes')
    verify_parser.add_argument('--hashfile', required=True, help='JSON file with saved hashes')
    verify_parser.add_argument('--dir', required=True, help='Directory to verify')

    # List command
    list_parser = subparsers.add_parser('list', help='List stored hashes')
    list_parser.add_argument('--hashfile', required=True, help='JSON file with saved hashes')

    return parser.parse_args()