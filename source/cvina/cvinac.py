# cvinac.py
import sys
from cvina import run_cvina_code, CvinaError

# ANSI escape codes for colors
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def run_file(filename):
    try:
        with open(filename, "r") as f:
            code = f.read()
        run_cvina_code(code, filename)
    except FileNotFoundError:
        print(f"error: File '{filename}' not found")
    except CvinaError as e:
        print(e)

def show_welcome():
    print(f"{BLUE}Cvina 1.0.0{RESET}")
    print(f"    {YELLOW}Please open a file!{RESET}")
    print("    Docs: https://cvina-lang.github.io/docs")
    print("    Website: https://cvina-lang.github.io")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_welcome()
        sys.exit(0)
    
    run_file(sys.argv[1])