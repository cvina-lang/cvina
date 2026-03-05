# cvina.py
import sys

# ANSI escape for red text
RED = "\033[31m"
RESET = "\033[0m"

class CvinaError(Exception):
    def __init__(self, msg, line=None, line_text=None):
        self.msg = msg
        self.line = line
        self.line_text = line_text
        super().__init__(msg)
    
    def __str__(self):
        preview = f", ({self.line_text.strip()})" if self.line_text else ""
        err_line = f"    line {self.line}{preview}\n      ^" if self.line else ""
        return f"{RED}error:{RESET} {self.msg}\n{err_line}\n<End of error>"

# Map Cvina keywords to Python
KEYWORD_MAP = {
    "printw": "print",
    "fn": "def",
    "class": "class",
    "#include": "import",
}

def run_cvina_code(code_str, filename="<string>"):
    lines = code_str.splitlines()
    translated_lines = []
    
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("#include"):
            # Support #include("module") syntax
            try:
                import_name = stripped.split('(')[1].split(')')[0].strip('"').strip("'")
                translated_lines.append(f"import {import_name}")
            except Exception:
                raise CvinaError("Invalid include syntax", i, line)
            continue
        
        # Replace keywords
        for k, v in KEYWORD_MAP.items():
            if k in line:
                line = line.replace(k, v)
        translated_lines.append(line)
    
    python_code = "\n".join(translated_lines)
    try:
        exec(python_code, globals())
    except Exception as e:
        tb = sys.exc_info()[2]
        error_line = lines[tb.tb_lineno - 1] if tb.tb_lineno <= len(lines) else None
        raise CvinaError(f"{type(e).__name__}: {str(e)}", tb.tb_lineno, error_line)