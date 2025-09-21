# Wit Version Control

A custom version control system built in Python that replicates essential Git functionality. Wit provides a simple command-line interface for managing file versions and tracking changes in your projects.

## Features

- **Repository Management**: Initialize new repositories with `wit init`
- **Staging Area**: Add files to staging with `wit add <filename>`
- **Version Control**: Commit changes with messages using `wit commit <message>`
- **History Tracking**: View commit history with `wit log`
- **Status Monitoring**: Check repository status with `wit status`
- **Version Navigation**: Switch between commits using `wit checkout <hash>`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MiriAppel/wit-version-control.git
cd wit-version-control
```
2. Install dependencies:
```bash
pip install click
```
3. Run wit commands:
```bash
python main.py init         # Or use wit.bat on Windows
```

## Quick Start

```bash
wit init                    # Initialize repository
wit add myfile.txt         # Stage file
wit commit "First commit"  # Commit changes
wit log                    # View history
wit status                 # Check status
```

## Architecture

- **Object-Oriented Design**: Clean class structure with Repository, CommitVersion, and CLI classes
- **Modular Code**: Separated concerns with dedicated modules for file operations and version management
- **Command Pattern**: CLI interface using Click framework

## Built With

- Python 3.x
- Click (Command Line Interface)
- JSON (Metadata storage)

Perfect for learning version control concepts or as a lightweight alternative to Git for simple projects.
