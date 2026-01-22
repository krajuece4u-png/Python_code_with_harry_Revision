#!/usr/bin/env python3
"""
Script to remove all solutions from practice files
"""
import re
from pathlib import Path

PRACTICE_SETS = [
    "01_SETUP_PRACTICE_SET",
    "02_PYTHON_SYNTEX_PRACTICE_SET",
    "03_VARIABLES_PRACTICE_SET",
    "04_TYPECASTING_PRACTICE_SET",
    "05_USER_INPUT_PRACTICE_SET",
    "06_COMMENT_ESCAPE_PRINT_PRACTICE_SET",
    "07_OPERATORS_PRACTICE_SET",
    "08_CONDITION_PRACTICE_SET",
    "09_LOOPS_PRACTICE_SET",
    "10_STRINGS_PRACTICE_SET",
    "11_FUNCTION_PRACTICE_SET",
    "12_LIST_PRACTICE_SET",
    "13_TUPLES_PRACTICE_SET",
]

FILE_TYPES = ["simple.py", "moderate.py", "hard.py"]

def clean_solution_file(filepath):
    """Remove all solution code, keep only structure with TODO comments"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    cleaned_lines = []
    in_docstring = False
    docstring_marker = None
    
    for line in lines:
        # Handle docstrings
        if '"""' in line or "'''" in line:
            marker = '"""' if '"""' in line else "'''"
            if not in_docstring:
                in_docstring = True
                docstring_marker = marker
                cleaned_lines.append(line)
            else:
                if marker == docstring_marker:
                    in_docstring = False
                    docstring_marker = None
                cleaned_lines.append(line)
            continue
        
        if in_docstring:
            cleaned_lines.append(line)
            continue
        
        # Keep comments with problem descriptions
        if line.strip().startswith('#'):
            cleaned_lines.append(line)
            continue
        
        # Keep print statements with problem headers (===)
        if 'print(' in line and '===' in line:
            cleaned_lines.append(line)
            continue
        
        # Keep print statements describing the problem
        if 'print(' in line and ('Write' in line or 'problem' in line.lower()):
            cleaned_lines.append(line)
            continue
        
        # Keep TODO comments
        if 'TODO' in line or 'todo' in line.lower():
            cleaned_lines.append(line)
            continue
        
        # Keep empty lines
        if not line.strip():
            cleaned_lines.append(line)
            continue
        
        # Skip everything else (solutions)
        pass
    
    cleaned_content = '\n'.join(cleaned_lines)
    
    # Clean up excessive empty lines
    cleaned_content = re.sub(r'\n\n\n+', '\n\n', cleaned_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    return filepath

# Main execution
base_path = Path(__file__).parent

total_files = 0
cleaned_files = 0

for practice_set in PRACTICE_SETS:
    folder = base_path / practice_set
    if folder.exists():
        for file_type in FILE_TYPES:
            filepath = folder / file_type
            if filepath.exists():
                total_files += 1
                try:
                    clean_solution_file(filepath)
                    cleaned_files += 1
                    print(f"✓ Cleaned: {practice_set}/{file_type}")
                except Exception as e:
                    print(f"✗ Error cleaning {practice_set}/{file_type}: {e}")
    else:
        print(f"✗ Folder not found: {practice_set}")

print(f"\n{'='*60}")
print(f"Total files processed: {cleaned_files}/{total_files}")
print(f"{'='*60}")
