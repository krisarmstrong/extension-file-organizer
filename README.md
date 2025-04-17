# Extension File Organizer

[![CI](https://github.com/krisarmstrong/extension-file-organizer/actions/workflows/ci.yml/badge.svg)](https://github.com/krisarmstrong/extension-file-organizer/actions)
[![Coverage](https://img.shields.io/badge/coverage-80%25-green)](https://github.com/krisarmstrong/extension-file-organizer)
[![PyPI](https://img.shields.io/pypi/v/extension-file-organizer.svg)](https://pypi.org/project/extension-file-organizer/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/krisarmstrong/extension-file-organizer/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)

## Overview
A CLI utility to group files by extension into subfolders and rename each file with a `YYYY-MM-<original_name>` prefix based on its last modification time.

- **Author**: Kris Armstrong
- **Version**: 1.0.1
- **License**: MIT

## Installation
```bash
git clone git@github.com:krisarmstrong/extension-file-organizer.git
cd extension-file-organizer
```

## Usage
```bash
python extension_file_organizer.py --source /path/to/dir --logfile log.txt --verbose
```

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for fork-branch-PR guidelines.

## License
MIT License. See [LICENSE](LICENSE) for details.