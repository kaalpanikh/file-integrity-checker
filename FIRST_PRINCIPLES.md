# Understanding File Integrity Checker from First Principles

## 1. Basic Concepts

### 1.1 What is a File?
- A file is a collection of data stored on a computer
- Examples: text documents, images, programs
- Files can be:
  - Read (viewed)
  - Written (modified)
  - Created
  - Deleted

### 1.2 Why Files Need Protection
- Files can be changed by:
  - Authorized users (good changes)
  - Malware (bad changes)
  - System errors (accidental changes)
- We need to know if changes happened

### 1.3 What is a Hash?
1. **Simple Example**:
   ```python
   Text: "hello"
   Hash: "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
   
   Text: "Hello"  # Just changed 'h' to 'H'
   Hash: "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
   ```
   - Completely different hash for a tiny change!

2. **Properties**:
   - Always same length output
   - Same input = Same hash
   - Different input = Different hash (almost always)
   - Can't go backwards from hash to file

## 2. Tools We Use

### 2.1 Python Programming Language
1. **What is Python?**
   - A programming language that's easy to read
   - Comes with many useful tools
   - Good for beginners

2. **Why Python?**
   - Has built-in security features
   - Easy to write command-line programs
   - Large community and help available

### 2.2 Command Line Interface (CLI)
1. **What is CLI?**
   - Text-based way to use computer
   - Type commands instead of clicking
   - More powerful than graphical interface

2. **Basic Commands**:
   ```bash
   # List files
   ls
   
   # Change directory
   cd some_folder
   
   # Run our program
   python integrity_checker.py
   ```

## 3. Building Our Program Step by Step

### 3.1 Setting Up (One Time Setup)
1. **Create Project Folder**:
   ```bash
   # Make a new folder
   mkdir file-integrity-checker
   
   # Go into the folder
   cd file-integrity-checker
   ```

2. **Install Python Packages**:
   ```bash
   # Create requirements.txt
   click==8.1.7      # For making CLI programs
   pathlib==1.0.1    # For working with files
   PyYAML==6.0.1     # For storing data
   
   # Install them
   pip install -r requirements.txt
   ```

### 3.2 Core Program Parts

#### 1. Reading Files
```python
# Bad way (whole file at once):
content = open(file_path).read()  # Might crash with big files

# Good way (piece by piece):
with open(file_path, "rb") as f:
    while True:
        piece = f.read(4096)  # Read 4KB at a time
        if not piece:
            break
        # Process this piece
```

#### 2. Creating Hashes
```python
# Step 1: Create hash calculator
hash_calculator = hashlib.sha256()

# Step 2: Feed it file contents
hash_calculator.update(some_data)

# Step 3: Get final hash
final_hash = hash_calculator.hexdigest()
```

#### 3. Storing Information
```python
# In .file_hashes.yml:
/path/to/file1.txt: "hash1..."
/path/to/file2.txt: "hash2..."
```

### 3.3 Main Commands

#### 1. Initialize Command
```python
# When user types: ./integrity-check init some_file.txt

1. Check if file exists
2. Calculate its hash
3. Store hash in .file_hashes.yml
4. Tell user it worked
```

#### 2. Check Command
```python
# When user types: ./integrity-check check some_file.txt

1. Load stored hash from .file_hashes.yml
2. Calculate current hash
3. Compare them
4. Tell user if they match
```

#### 3. Update Command
```python
# When user types: ./integrity-check update some_file.txt

1. Calculate new hash
2. Update stored hash
3. Tell user it worked
```

## 4. How to Use the Program

### 4.1 Basic Usage
1. **First Time Setup**:
   ```bash
   # Create a test file
   echo "Hello, World!" > important.txt
   
   # Initialize its hash
   ./integrity-check init important.txt
   ```

2. **Checking Files**:
   ```bash
   # Check if file changed
   ./integrity-check check important.txt
   
   # Should say: Status: Unmodified
   ```

3. **After Changes**:
   ```bash
   # Change the file
   echo "New content" > important.txt
   
   # Check again
   ./integrity-check check important.txt
   
   # Should say: Status: Modified (Hash mismatch)
   ```

### 4.2 Common Tasks

1. **Checking Multiple Files**:
   ```bash
   # Initialize a whole folder
   ./integrity-check init my_folder
   
   # Check all files in folder
   ./integrity-check check my_folder
   ```

2. **After Making Changes**:
   ```bash
   # Update hash after legitimate changes
   ./integrity-check update changed_file.txt
   ```

## 5. Understanding the Code

### 5.1 Main Function Explanations

1. **Hash Calculation**:
   ```python
   def calculate_file_hash(file_path: str) -> str:
       # Create new hash calculator
       sha256_hash = hashlib.sha256()
       
       # Open file safely
       with open(file_path, "rb") as f:
           # Read file piece by piece
           for byte_block in iter(lambda: f.read(4096), b""):
               # Update hash with each piece
               sha256_hash.update(byte_block)
       
       # Get final hash
       return sha256_hash.hexdigest()
   ```
   
   What each part does:
   - `hashlib.sha256()`: Creates new hash calculator
   - `open(file_path, "rb")`: Opens file in binary mode
   - `read(4096)`: Reads 4KB chunks
   - `update()`: Adds data to hash
   - `hexdigest()`: Gets final hash string

2. **Hash Storage**:
   ```python
   def save_hashes(hashes: Dict[str, str]):
       # Open file for writing
       with open(HASH_FILE, 'w') as f:
           # Save hashes in YAML format
           yaml.dump(hashes, f)
   ```
   
   What each part does:
   - `open(HASH_FILE, 'w')`: Creates/opens file
   - `yaml.dump()`: Saves data in readable format

## 6. Common Problems and Solutions

### 6.1 When Things Go Wrong

1. **File Not Found**:
   ```python
   # Problem: File doesn't exist
   FileNotFoundError: [Errno 2] No such file or directory
   
   # Solution: Check if file exists first
   if not os.path.exists(file_path):
       print("File not found!")
       return
   ```

2. **Permission Denied**:
   ```python
   # Problem: Can't read/write file
   PermissionError: [Errno 13] Permission denied
   
   # Solution: Check permissions or run as administrator
   ```

### 6.2 Good Practices

1. **Always Close Files**:
   ```python
   # Bad way:
   f = open(file)
   # File stays open
   
   # Good way:
   with open(file) as f:
       # File closes automatically
   ```

2. **Check Inputs**:
   ```python
   # Bad way:
   process_file(user_input)
   
   # Good way:
   if os.path.exists(user_input):
       process_file(user_input)
   else:
       print("File not found!")
   ```

## 7. Learning More

### 7.1 Next Steps
1. Learn about different hash types (MD5, SHA-1, SHA-256)
2. Study file system permissions
3. Explore Python's security features
4. Learn about encryption

### 7.2 Practice Ideas
1. Add new features:
   - Email notifications
   - Scheduled checks
   - GUI interface
2. Improve error handling
3. Add more hash algorithms

## 8. Getting Help

### 8.1 When Stuck
1. Read error messages carefully
2. Check Python documentation
3. Search Stack Overflow
4. Ask clear questions
5. Try simpler test cases

### 8.2 Resources
1. Python Documentation
2. Security Blogs
3. Programming Forums
4. Online Courses

Remember: Learning takes time. Start with basics and build up gradually!
