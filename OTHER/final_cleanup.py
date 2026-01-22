#!/usr/bin/env python3
"""
Final comprehensive cleanup
"""
from pathlib import Path
import re

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

def final_cleanup(filepath):
    """Final comprehensive cleanup"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove all solution code patterns
    content = re.sub(r'# Solution:.*', '', content, flags=re.DOTALL)
    content = re.sub(r'# SOLUTION:.*', '', content, flags=re.DOTALL)
    content = re.sub(r'# solution:.*', '', content, flags=re.DOTALL)
    
    # Add TODO comments after PROBLEM headers if missing
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        fixed_lines.append(line)
        
        # If this is a print with === and next line is empty, add TODO
        if '===' in line and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if not next_line or (i + 2 < len(lines) and lines[i + 2].strip() == ''):
                if i + 2 < len(lines) and 'TODO' not in lines[i + 2]:
                    fixed_lines.append('\n# TODO: Write your solution here')
    
    # Remove excessive empty lines
    result = '\n'.join(fixed_lines)
    result = re.sub(r'\n\n\n+', '\n\n', result)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)

# Main
base_path = Path(__file__).parent

for practice_set in PRACTICE_SETS:
    folder = base_path / practice_set
    if folder.exists():
        for file_type in FILE_TYPES:
            filepath = folder / file_type
            if filepath.exists():
                try:
                    final_cleanup(filepath)
                    print(f"✓ Final cleanup: {practice_set}/{file_type}")
                except Exception as e:
                    print(f"✗ Error: {e}")

print(f"\nAll files cleaned!")
