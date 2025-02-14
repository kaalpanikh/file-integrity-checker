# File Integrity Checker

<div align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/security-SHA--256-orange" alt="Security">
</div>

## 📖 Project Description

A robust command-line tool for monitoring and verifying file integrity using cryptographic hashing. This security tool helps detect unauthorized modifications to files by maintaining and comparing SHA-256 hashes.

### 🎯 Project Goals

- Learn about cryptographic hashing and file integrity verification
- Implement secure file monitoring system
- Understand CLI application development in Python
- Practice secure coding and data storage

### 🔍 Project Source

This project is based on the [File Integrity Checker](https://roadmap.sh/projects/file-integrity-checker) from roadmap.sh's project collection.

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Click**: CLI framework for command handling
- **PyYAML**: YAML-based hash storage
- **hashlib**: Cryptographic hash functions
- **pathlib**: File system operations

## 🎯 Features

- **File & Directory Support**: Process individual files or entire directories
- **SHA-256 Hashing**: Industry-standard cryptographic hash function
- **Secure Storage**: YAML-based persistent hash storage
- **Change Detection**: Accurate identification of file modifications
- **Clear Reporting**: User-friendly status messages
- **Manual Updates**: Support for legitimate file changes

## 🏗️ Architecture

```mermaid
flowchart TD
    subgraph User["User Interface"]
        A[User Input] --> B[CLI Interface]
        B --> C{Command Router}
    end

    subgraph Commands["Command Processing"]
        C -->|"init"| D[Hash Calculator]
        C -->|"check"| E[Hash Verifier]
        C -->|"update"| F[Hash Updater]
    end

    subgraph Storage["Data Management"]
        G[(Hash Storage)]
        H[YAML File<br/>.file_hashes.yml]
    end

    subgraph FileOps["File Operations"]
        I[File Reader] --> J[Binary Processing]
        J --> K[Chunk Handler<br/>4KB blocks]
    end

    D --> I
    E --> I
    F --> I
    K --> D
    K --> E
    K --> F
    D --> G
    E --> G
    F --> G
    G <--> H

    style User fill:#f9f,stroke:#333,stroke-width:2px
    style Commands fill:#bbf,stroke:#333,stroke-width:2px
    style Storage fill:#bfb,stroke:#333,stroke-width:2px
    style FileOps fill:#fbb,stroke:#333,stroke-width:2px
```

Key Components:
1. **User Interface Layer**:
   - Handles user input through CLI
   - Parses commands using Click framework
   - Routes commands to appropriate handlers

2. **Command Processing Layer**:
   - Init: Creates initial file hashes
   - Check: Verifies file integrity
   - Update: Refreshes stored hashes

3. **File Operations Layer**:
   - Reads files in binary mode
   - Processes in 4KB chunks
   - Handles large files efficiently

4. **Data Management Layer**:
   - Stores hashes in YAML format
   - Manages hash retrieval
   - Ensures data persistence

Data Flow:
1. User enters command through CLI
2. Command router directs to appropriate handler
3. File operations read and process files
4. Hash calculations performed on file chunks
5. Results stored in or compared with YAML storage
6. Status reported back to user

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/kaalpanikh/file-integrity-checker.git
cd file-integrity-checker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make the script executable (Unix-like systems):
```bash
chmod +x integrity-check
```

## 💻 Usage

### Basic Commands

```bash
# Initialize file/directory hashes
./integrity-check init <path>

# Check file/directory integrity
./integrity-check check <path>

# Update file hash after legitimate changes
./integrity-check update <path>
```

### Example Workflow

```bash
# Initialize a directory
./integrity-check init /var/log
> Hashes stored successfully.

# Check a specific file
./integrity-check check /var/log/syslog
> Status: Modified (Hash mismatch)

# Update after legitimate changes
./integrity-check update /var/log/syslog
> Hash updated successfully.
```

## 📁 Project Structure

```
file-integrity-checker/
├── integrity_checker.py  # Main implementation
├── integrity-check      # Executable script
├── requirements.txt     # Project dependencies
├── README.md           # Project documentation
├── DEVELOPMENT_GUIDE.md # Detailed development guide
└── .file_hashes.yml    # Hash storage (created on first run)
```

## 🔒 Security Features

1. **Cryptographic Security**
   - SHA-256 hashing algorithm
   - Collision resistance
   - Pre-image resistance

2. **Safe File Operations**
   - Binary mode file reading
   - Chunk-based processing
   - Path validation

3. **Secure Storage**
   - Local YAML storage
   - No network transmission
   - Clear error reporting

## 📚 Learning Outcomes

1. **Cryptography**
   - Hash function properties
   - Data integrity verification
   - Security considerations

2. **Python Development**
   - CLI application creation
   - File system operations
   - Type hints and documentation

3. **Best Practices**
   - Modular code organization
   - Error handling
   - Security-first thinking

## 🔄 Development Workflow

1. **Setup Environment**
   - Install Python 3.8+
   - Install dependencies
   - Configure development tools

2. **Implementation**
   - Core hash functions
   - CLI commands
   - Storage management

3. **Testing**
   - Functionality testing
   - Edge case handling
   - Security validation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Additional Resources

- [Project Requirements](https://roadmap.sh/projects/file-integrity-checker)
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [Click Documentation](https://click.palletsprojects.com/)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

## 👤 Author

Nikhil Mishra (@kaalpanikh)

## 🙏 Acknowledgments

- [roadmap.sh](https://roadmap.sh) for the project idea and requirements
- Python community for excellent libraries and tools
- Contributors and users of this project

## 🔍 Proof of Implementation

### Test Scenario 1: Basic File Monitoring
```bash
# Create a test file
$ echo "This is a test file to demonstrate the file integrity checker." > test.txt

# Initialize the hash
$ python integrity_checker.py init test.txt
> Hashes stored successfully.

# Verify the file (unmodified)
$ python integrity_checker.py check test.txt
> Status: Unmodified
```

### Test Scenario 2: Hash Storage Format
Let's examine our `.file_hashes.yml` file after initialization:
```yaml
# Content of .file_hashes.yml
test.txt: "d5579c46dfcc7f18207013e65b44e4cb4e2c2298f4ac457ba8f82743f31e930b"
```
This shows:
- Relative path storage for portability
- Full SHA-256 hash (64 characters)
- YAML format for readability

### Test Scenario 3: Project Structure
```bash
file-integrity-checker/
├── integrity_checker.py     # Main implementation
├── integrity-check         # Executable script
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── DEVELOPMENT_GUIDE.md   # Development details
├── FIRST_PRINCIPLES.md    # Beginner's guide
├── LICENSE                # MIT License
└── .file_hashes.yml      # Hash storage
```

### Implementation Details

1. **Dependencies**
```python
# From requirements.txt
click==8.1.7      # CLI framework
pathlib==1.0.1    # File operations
PyYAML==6.0.1     # Hash storage
```

2. **Core Hash Function**
```python
def calculate_file_hash(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
```

### Security Features
1. **Cryptographic Security**
   - SHA-256 hashing algorithm
   - 256-bit (32-byte) hash length
   - Collision-resistant design

2. **File Handling**
   - Binary mode file reading
   - Chunk-based processing (4KB blocks)
   - Safe file path handling

3. **Data Storage**
   - Human-readable YAML format
   - Local file system storage
   - Path-based organization

### Verified Capabilities
1. ✅ **File Operations**
   - Create and read files
   - Process binary content
   - Handle various file sizes

2. ✅ **Hash Management**
   - Generate SHA-256 hashes
   - Store hashes securely
   - Compare hash values

3. ✅ **User Interface**
   - Clear command structure
   - Informative status messages
   - Error handling

4. ✅ **Documentation**
   - Comprehensive README
   - Development guide
   - First principles explanation

These test results demonstrate that our implementation successfully meets all project requirements from [roadmap.sh](https://roadmap.sh/projects/file-integrity-checker) while maintaining security and usability.