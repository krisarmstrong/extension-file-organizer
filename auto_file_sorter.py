#!/usr/bin/env python3
"""
Auto File Sorter

Groups files in a source directory by file extension and renames each
file with a "YYYY-MM-<original_name>.<ext>" prefix based on its last-
modification timestamp.

Version: 1.0.0
Author: Your Name
Platform: Linux, macOS, Windows
Python: 3.6+
"""

import os
import shutil
import argparse
import logging
import sys
from datetime import datetime

__version__ = "1.0.0"


def setup_logging(verbose: bool, logfile: str = None):
    """
    Configure logging output to console and optional logfile.

    Args:
        verbose (bool): Enable DEBUG-level logging if True.
        logfile (str): Path to file for logging output (optional).
    """
    logger = logging.getLogger()
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)
    ch.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    logger.addHandler(ch)

    # File handler
    if logfile:
        fh = logging.FileHandler(logfile)
        fh.setLevel(level)
        fh.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
        logger.addHandler(fh)


def get_year_month_prefix(path: str) -> str:
    """
    Return a 'YYYY-MM' string based on file's last modification time.

    Args:
        path (str): File path.
    Returns:
        str: Formatted year-month prefix.
    """
    try:
        ts = os.path.getmtime(path)
    except Exception as e:
        logging.warning("Could not get modification time for %s: %s", path, e)
        ts = datetime.now().timestamp()
    return datetime.fromtimestamp(ts).strftime("%Y-%m")


def organize_by_extension(source_dir: str, logfile: str):
    """
    Walks through source_dir, groups files by extension into subfolders,
    and renames them with a 'YYYY-MM-' prefix.

    Args:
        source_dir (str): Path to directory to organize.
        logfile (str): File path for runtime logs.
    """
    for root, _, files in os.walk(source_dir):
        for name in files:
            src = os.path.join(root, name)
            if not os.path.isfile(src):
                continue

            prefix = get_year_month_prefix(src)
            ext = os.path.splitext(name)[1].lstrip('.').lower() or 'no_extension'
            dest_dir = os.path.join(source_dir, ext)
            os.makedirs(dest_dir, exist_ok=True)

            new_name = f"{prefix}-{name}"
            dest = os.path.join(dest_dir, new_name)

            try:
                shutil.move(src, dest)
                logging.info("Moved %s -> %s", src, dest)
            except Exception as e:
                logging.error("Failed to move %s: %s", src, e)


def main():
    """
    Entry point: parse arguments, set up logging, and run organizer.
    """
    parser = argparse.ArgumentParser(
        description="Auto File Sorter: group by extension and prepend year-month"
    )
    parser.add_argument('--source', '-s', required=True,
                        help='Source directory to organize')
    parser.add_argument('--logfile', '-l', default=None,
                        help='Optional log file for runtime logs')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Enable debug-level logging')

    args = parser.parse_args()
    setup_logging(args.verbose, args.logfile)

    try:
        organize_by_extension(args.source, logfile=args.logfile)
    except KeyboardInterrupt:
        logging.info("Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        logging.critical("Unhandled exception: %s", e)
        sys.exit(1)


if __name__ == '__main__':
    main()
