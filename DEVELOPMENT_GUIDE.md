# File Integrity Checker - Beginner's Development Guide

This guide explains every aspect of building the File Integrity Checker project, written specifically for beginners. We'll cover not just what we did, but why we did it and how it works.

## Part 1: Understanding the Basics

### What is File Integrity?
- **Definition**: File integrity means making sure a file hasn't been changed or tampered with
- **Example**: Imagine leaving a document in a drawer and wanting to know if someone changed it while you were away
- **Real-world analogy**: It's like a seal on medicine bottles that shows if they've been opened

### Why Do We Need This Tool?
1. **Security**: Detect unauthorized changes to important files
2. **Compliance**: Many organizations need to prove their files haven't been modified
3. **Troubleshooting**: Identify when and which files have changed

### How Does It Work?
1. **Hashing Explained**:
   - A hash is like a unique fingerprint for a file
   - Even tiny changes to the file create a completely different fingerprint
   - Example: The text "hello" might hash to "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
   - Change it to "Hello" and the hash completely changes

2. **Our Process**:
   ```
   Original File → Calculate Hash → Store Hash
        ↓
   Later Check → Calculate New Hash → Compare with Stored Hash
   ```

## Part 2: Setting Up the Project

### 1. Creating Project Structure
```bash
file-integrity-checker/
├── integrity_checker.py  # Our main program
├── requirements.txt      # List of required packages
└── .file_hashes.yml     # Where we store our hashes
```

### 2. Required Tools and Why We Need Them
1. **Python (3.8+)**
   - Why: Modern features, good security libraries
   - What it does: Our main programming language

2. **click Package**
   - Why: Makes command-line tools easy to create
   - What it does: Handles user commands and arguments

3. **PyYAML Package**
   - Why: Easy to read and write data files
   - What it does: Stores our file hashes

4. **hashlib Module**
   - Why: Built-in secure hashing functions
   - What it does: Creates file fingerprints

### 3. Installing Dependencies
```python
# requirements.txt content:
click==8.1.7      # For command-line interface
pathlib==1.0.1    # For file operations
PyYAML==6.0.1     # For storing hashes
```

## Part 3: Building the Core Features

### 1. File Hash Calculation
```python
def calculate_file_hash(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
```

Let's break this down:
- `hashlib.sha256()`: Creates a new SHA-256 hash calculator
- `open(file_path, "rb")`: Opens file in binary mode (works with all file types)
- `read(4096)`: Reads 4KB at a time (good for large files)
- `hexdigest()`: Converts hash to readable text

### 2. Hash Storage System
```python
def save_hashes(hashes: Dict[str, str]):
    with open(HASH_FILE, 'w') as f:
        yaml.dump(hashes, f)
```

What's happening:
- Uses YAML format (easy to read)
- Stores as key-value pairs:
  ```yaml
  /path/to/file1.txt: "hash1..."
  /path/to/file2.txt: "hash2..."
  ```

### 3. Command Interface
We created three main commands:

1. **init**: First-time setup
   ```python
   @cli.command()
   @click.argument('path')
   def init(path: str):
       # Calculate and store initial hashes
   ```

2. **check**: Verify files
   ```python
   @cli.command()
   @click.argument('path')
   def check(path: str):
       # Compare current vs stored hashes
   ```

3. **update**: Update stored hashes
   ```python
   @cli.command()
   @click.argument('path')
   def update(path: str):
       # Update stored hash for a file
   ```

## Part 4: Security Features

### 1. Why SHA-256?
- Industry standard security
- Virtually impossible to:
  - Create a file with a specific hash
  - Find two files with the same hash
  - Reverse a hash back to the file

### 2. Safe File Handling
- Read files in binary mode (works with all file types)
- Process in chunks (handles large files)
- Careful path handling (prevents security issues)

### 3. Error Handling
- Check if files exist
- Validate input paths
- Clear error messages

## Part 5: Testing the Project

### 1. Basic Test Scenario
```bash
# Create a test file
echo "Hello, World!" > test.txt

# Initialize hash
./integrity-check init test.txt

# Verify it works
./integrity-check check test.txt
# Should show: Status: Unmodified

# Make a change
echo "Modified!" > test.txt

# Check again
./integrity-check check test.txt
# Should show: Status: Modified (Hash mismatch)
```

### 2. What to Test
1. Single files
2. Entire directories
3. Large files
4. Different file types
5. Error cases (missing files, permissions)

## Part 6: Common Questions

### 1. "Why use YAML for storage?"
- Human-readable format
- Easy to debug
- Built-in Python support

### 2. "Why process files in chunks?"
- Memory efficient
- Can handle very large files
- Doesn't slow down the computer

### 3. "What makes SHA-256 secure?"
- Very long hash (256 bits)
- Small changes cause big hash changes
- Mathematically difficult to fake

## Part 7: Learning Outcomes

### 1. Python Skills Learned
- File operations
- Command-line interfaces
- Type hints
- Error handling
- Working with packages

### 2. Security Concepts
- Cryptographic hashing
- File integrity
- Secure storage
- Input validation

### 3. Best Practices
- Code organization
- Documentation
- Error handling
- User interface design

## Part 8: Next Steps

### 1. Possible Enhancements
- Add more hash algorithms
- Real-time file monitoring
- Email notifications
- Web interface

### 2. Learning Path
1. Study cryptography basics
2. Learn about file systems
3. Explore Python packaging
4. Practice secure coding

## Need Help?

If you're stuck:
1. Read the error message carefully
2. Check the README.md
3. Try the examples
4. Ask specific questions
5. Look at similar projects

Remember: Every developer was a beginner once. Don't be afraid to experiment and learn from mistakes!
