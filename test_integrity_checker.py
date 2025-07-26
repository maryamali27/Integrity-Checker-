# (Unit Tests)
#!/usr/bin/env python3
import shutil
"""
Unit tests for the Integrity Checker.
"""
import os
import tempfile
from hasher import hash_file, compute_hashes

def test_hashing():
    """Test hash computation for a sample file."""
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile.write(b"test data")
        tmpfile_path = tmpfile.name
    
    hash_val = hash_file(tmpfile_path)
    assert len(hash_val) == 64  # SHA-256 produces 64 hex chars
    os.remove(tmpfile_path)

def test_directory_hashing():
    """Test recursive hashing of a directory."""
    os.makedirs("test_dir", exist_ok=True)
    with open("test_dir/file1.txt", "w") as f:
        f.write("content1")
    with open("test_dir/file2.txt", "w") as f:
        f.write("content2")
    
    hashes = compute_hashes("test_dir")
    assert len(hashes) == 2
    shutil.rmtree("test_dir")

if __name__ == "__main__":
    test_hashing()
    test_directory_hashing()
    print("All tests passed.")