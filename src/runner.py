import sys
import os

# Add the src folder to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(script_dir, "../src")
sys.path.insert(0, src_path)

from sparkup_lexer import lexer
from sparkup_parser import parser


def load_skp_file(filename):
    """Load and read a .skp file."""
    if not filename.endswith('.skp'):
        raise ValueError("Invalid file extension. Please use a .skp file.")
    with open(filename, 'r') as file:
        code = file.read()
    return code


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: skp <filename.skp>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        code = load_skp_file(filename)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Tokenizing the input
    lexer.input(code)
    for token in lexer:
        pass  # Tokenize the file content

    # Parsing the input code
    if parser.parse(code):
        print("Parsed successfully.")
    else:
        print("Parsing failed.")
