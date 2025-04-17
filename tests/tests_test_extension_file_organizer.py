import pytest
import subprocess
import sys

def test_cli_help():
    """Test CLI --help invocation."""
    result = subprocess.run(
        [sys.executable, "extension_file_organizer.py", "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Extension File Organizer" in result.stdout