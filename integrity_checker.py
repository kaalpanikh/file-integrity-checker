#!/usr/bin/env python3

import click
import hashlib
import os
import yaml
from pathlib import Path
from typing import Dict, Union

HASH_FILE = '.file_hashes.yml'

def calculate_file_hash(file_path: str) -> str:
    """Calculate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load_stored_hashes() -> Dict[str, str]:
    """Load stored hashes from YAML file."""
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return yaml.safe_load(f) or {}
    return {}

def save_hashes(hashes: Dict[str, str]):
    """Save hashes to YAML file."""
    with open(HASH_FILE, 'w') as f:
        yaml.dump(hashes, f)

@click.group()
def cli():
    """File Integrity Checker - A tool to monitor file modifications using hashes."""
    pass

@cli.command()
@click.argument('path')
def init(path: str):
    """Initialize and store hashes of files in the given path."""
    path = Path(path)
    stored_hashes = {}
    
    if path.is_file():
        stored_hashes[str(path)] = calculate_file_hash(str(path))
    elif path.is_dir():
        for file_path in path.rglob('*'):
            if file_path.is_file():
                stored_hashes[str(file_path)] = calculate_file_hash(str(file_path))
    
    save_hashes(stored_hashes)
    click.echo("Hashes stored successfully.")

@cli.command()
@click.argument('path')
def check(path: str):
    """Check if a file or directory has been modified."""
    path = Path(path)
    stored_hashes = load_stored_hashes()
    
    def check_single_file(file_path: Path):
        str_path = str(file_path)
        if str_path not in stored_hashes:
            click.echo(f"Status: Unknown (No stored hash for {str_path})")
            return
        
        current_hash = calculate_file_hash(str_path)
        if current_hash == stored_hashes[str_path]:
            click.echo(f"Status: Unmodified")
        else:
            click.echo(f"Status: Modified (Hash mismatch)")
    
    if path.is_file():
        check_single_file(path)
    elif path.is_dir():
        for file_path in path.rglob('*'):
            if file_path.is_file():
                click.echo(f"\nChecking: {file_path}")
                check_single_file(file_path)

@cli.command()
@click.argument('path')
def update(path: str):
    """Update the stored hash for a specific file."""
    path = Path(path)
    if not path.is_file():
        click.echo("Error: Please provide a valid file path")
        return
    
    stored_hashes = load_stored_hashes()
    stored_hashes[str(path)] = calculate_file_hash(str(path))
    save_hashes(stored_hashes)
    click.echo("Hash updated successfully.")

if __name__ == '__main__':
    cli()
