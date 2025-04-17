# Auto File Sorter

Version: 1.0.0

Groups files by extension into subfolders and renames each file with a
`YYYY-MM-<original_name>.<ext>` prefix based on last modification time.

## Installation

Ensure Python 3.6+ is installed. No external dependencies beyond the Python standard library.

```bash
chmod +x auto_file_sorter.py
```

## Usage

```bash
python auto_file_sorter.py --source /path/to/directory [--logfile logfile.log] [--verbose]
```

## Git Setup

Initialize a Git repository to track changes and versions:

```bash
git init
echo "__pycache__/
*.log
*.pyc
.DS_Store" > .gitignore
git add auto_file_sorter.py README.md CHANGELOG.md requirements.txt .gitignore
git commit -m "chore: initial release v1.0.0"
git tag -a v1.0.0 -m "v1.0.0"
```

Use your existing `bump_version.py` to bump versions and tag releases:
```bash
python bump_version.py patch
git commit -am "chore: bump to v1.X.Y"
git tag -a v1.X.Y -m "v1.X.Y"
```

