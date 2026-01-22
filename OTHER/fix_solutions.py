#!/usr/bin/env python3
"""
Enhanced cleanup script to fix corrupted lines
"""
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

def fix_corrupted_file(filepath):
    """Fix corrupted lines and solutions"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    skip_next = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Remove corrupted lines
        if 'prTODO' in stripped or 'Solution:' in stripped and i < len(lines) - 1:
            continue
        
        # Remove incomplete print statements (likely part of solution)
        if stripped.startswith('print(') and not ('===' in stripped or 'Write' in stripped or 'problem' in stripped.lower()):
            continue
        
        # Remove other solution code (non-comment, non-print lines)
        if stripped and not stripped.startswith('#') and not stripped.startswith('"') and not stripped.startswith("'"):
            if 'print(' not in stripped and 'TODO' not in stripped:
                # Skip lines that are likely solution code
                if not any(x in stripped for x in ['"""', "'''"]):
                    continue
        
        fixed_lines.append(line)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    return filepath

# Main execution
base_path = Path(__file__).parent

for practice_set in PRACTICE_SETS:
    folder = base_path / practice_set
    if folder.exists():
        for file_type in FILE_TYPES:
            filepath = folder / file_type
            if filepath.exists():
                try:
                    fix_corrupted_file(filepath)
                    print(f"✓ Fixed: {practice_set}/{file_type}")
                except Exception as e:
                    print(f"✗ Error fixing {practice_set}/{file_type}: {e}")

print(f"\n{'='*60}")
print(f"All practice files cleaned!")
print(f"{'='*60}")
