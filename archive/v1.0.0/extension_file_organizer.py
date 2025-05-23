#!/usr/bin/env python3
"""
Project Title: Extension File Organizer

A command-line utility that groups files in a source directory by file extension,
renaming each file with a "YYYY-MM-<original_name>" prefix based on its
last-modification timestamp.

Author: Kris Armstrong
"""

from __future__ import annotations
import argparse
import logging
import os
import shutil
import sys
from datetime import datetime
from typing import Optional

__version__ = "1.0.0"


def setup_logging(verbose: bool, logfile: Optional[str] = None) -> None:
    """
    Configure logging output to console and optional logfile.

    Args:
        verbose (bool): If True, set log level to DEBUG; else INFO.
        logfile (Optional[str]): Optional path to a file for logging output.
    """
    logger = logging.getLogger()
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    logger.addHandler(handler)
    if logfile:
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
        logger.addHandler(file_handler)


def get_year_month_prefix(path: str) -> str:
    """
    Return a 'YYYY-MM' prefix based on file's last modification time.

    Args:
        path (str): Path to the file.

    Returns:
        str: Formatted 'YYYY-MM'.
    """
    try:
        timestamp = os.path.getmtime(path)
    except OSError as e:
        logging.warning("Could not get mtime for %s: %s", path, e)
        timestamp = datetime.now().timestamp()
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m")


def organize_by_extension(source_dir: str) -> None:
    """
    Walk the source directory, group files by extension into subfolders,
    and rename each file with a year-month prefix.

    Args:
        source_dir (str): Path to the directory to organize.

    Raises:
        FileNotFoundError: If source_dir does not exist or is not a directory.
    """
    if not os.path.isdir(source_dir):
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    for root, _, files in os.walk(source_dir):
        for name in files:
            src_path = os.path.join(root, name)
            if not os.path.isfile(src_path):
                continue
            prefix = get_year_month_prefix(src_path)
            ext = os.path.splitext(name)[1].lstrip('.').lower() or 'no_extension'
            dest_dir = os.path.join(source_dir, ext)
            os.makedirs(dest_dir, exist_ok=True)
            new_name = f"{prefix}-{name}"
            dest_path = os.path.join(dest_dir, new_name)
            try:
                shutil.move(src_path, dest_path)
                logging.info("Moved %s -> %s", src_path, dest_path)
            except Exception as e:
                logging.error("Failed to move %s: %s", src_path, e)


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Extension File Organizer: group files by extension and rename with date prefix"
    )
    parser.add_argument(
        "--source", "-s", required=True,
        help="Source directory to organize"
    )
    parser.add_argument(
        "--logfile", "-l", default=None,
        help="Optional logfile path for runtime logs"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Enable debug-level logging"
    )
    parser.add_argument(
        "--version", action="version",
        version=f"%(prog)s {__version__}"
    )
    return parser.parse_args()


def main() -> None:
    """
    Entry point: parse arguments, configure logging, and run organizer.
    """
    args = parse_arguments()
    setup_logging(args.verbose, args.logfile)
    try:
        organize_by_extension(args.source)
    except KeyboardInterrupt:
        logging.info("Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        logging.critical("Fatal error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
