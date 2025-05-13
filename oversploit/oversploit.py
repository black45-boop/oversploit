import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.cli import OverSploitCLI

if __name__ == "__main__":
    OverSploitCLI().cmdloop()
