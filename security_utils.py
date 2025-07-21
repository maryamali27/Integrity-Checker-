# optional part of the code
#!/usr/bin/env python3
"""
Security utilities for signing hash databases.
"""
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

private_key = ec.generate_private_key(ec.SECP384R1())

def sign_hashes(hashes):
    """Sign a hash database with a private key."""
    hash_data = json.dumps(hashes).encode()
    signature = private_key.sign(hash_data, ec.ECDSA(hashes.SHA256()))
    return signature.hex()