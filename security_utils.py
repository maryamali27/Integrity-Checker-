# optional part of the code
#!/usr/bin/env python3
"""
Security utilities for signing hash databases.
"""
import json
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
# Remove unused imports: Encoding, PublicFormat

private_key = ec.generate_private_key(ec.SECP384R1())

def sign_hashes(hashes_dict):  # Renamed to avoid shadowing the 'hashes' module
    """Sign a hash database with a private key."""
    hash_data = json.dumps(hashes_dict).encode()
    signature = private_key.sign(hash_data, ec.ECDSA(hashes.SHA256()))  # Uses the hashes module
    return signature.hex()