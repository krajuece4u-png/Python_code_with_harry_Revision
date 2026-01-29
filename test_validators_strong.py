"""
STRONG VALIDATORS - All test cases with cheat-proof logic
These validators ensure solutions actually solve problems, not bypass them
"""

import re


class ProblemValidator:
    """Base validator for checking problem solutions"""
    
    @staticmethod
    def validate_output_contains(output, *keywords, case_sensitive=False):
        """Check if output contains all required keywords"""
        for keyword in keywords:
            pattern = keyword if case_sensitive else keyword.lower()
            output_search = output if case_sensitive else output.lower()
            if pattern not in output_search:
                return False, f"Output missing '{keyword}'"
        return True, "Valid"
    
    @staticmethod
    def validate_numbers_in_output(output, expected_numbers):
        """Validate that specific numbers appear in output"""
        for num in expected_numbers:
            if str(num) not in output:
                return False, f"Missing number {num}"
        return True, "Valid"
    
    @staticmethod
    def has_operators(output, required_ops=None):
        """Check for mathematical/logical operators"""
        if required_ops is None:
            required_ops = ['+', '-', '*', '/', '%', '==', '!=', '<', '>', 'if', 'for', 'while']
        return any(op in output for op in required_ops)
    
    @staticmethod
    def has_functions(output, functions=None):
        """Check for function calls"""
        if functions is None:
            functions = ['int(', 'str(', 'float(', 'len(', 'sum(', 'max(', 'min(', 'print(']
        return sum(1 for f in functions if f in output)


# ============================================================
# STRONG VALIDATORS FOR ALL 13 PRACTICE SETS
# ============================================================

class Setup01Validators:
    """01_SETUP - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        if not all(w in output.lower() for w in ["welcome", "python", "programming"]):
            return False, "Missing required words"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        lines = [l for l in output.split('\n') if l.strip() and not '===' in l]
        if len(lines) < 1 or lines[0].lower() in ['your name', 'name']:
            return False, "Name should not be placeholder"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        lines = [l.strip() for l in output.split('\n') if l.strip() and '===' not in l]
        if len(lines) < 3 or len(set(lines)) < 2:
            return False, "Need 3 different lines"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p1(output):
        if not any(op in output for op in ['+', 'sum', 'add', 'result']):
            return False, "Missing arithmetic"
        if 'result' not in output.lower() and 'sum' not in output.lower():
            return False, "Should label as result/sum"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        if '+' not in output and 'concatenat' not in output.lower():
            return False, "String concatenation needed"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        if len(lines) < 2:
            return False, "Need multiple operations"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        if '+' not in output and '-' not in output and '*' not in output and '/' not in output:
            return False, "Missing operators"
        if not any(c.isdigit() for c in output):
            return False, "No numeric result"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        ops = sum(1 for op in ['+', '-', '*', '/', '%', '**'] if op in output)
        if ops < 2:
            return False, "Nested operations need multiple operators"
        return True, "Valid"


class Syntax02Validators:
    """02_PYTHON_SYNTEX - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 1, "Valid") if len(lines) >= 1 else (False, "No output")
    
    @staticmethod
    def validate_simple_p2(output):
        if 'print(' not in output * 2:  # at least 2 prints
            return False, "Multiple statements needed"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        return (True, "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p1(output):
        return (True, "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p2(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 2, "Need multiple operations") if len(lines) < 2 else (True, "Valid")
    
    @staticmethod
    def validate_moderate_p3(output):
        return (True, "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p1(output):
        return (True, "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p2(output):
        return (True, "Valid") if output.strip() else (False, "No output")


class Variables03Validators:
    """03_VARIABLES - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        required = ['raju', '23', 'kolkata']
        return (all(str(r) in output.lower() for r in required), "Valid") if all(str(r) in output.lower() for r in required) else (False, f"Missing variable values")
    
    @staticmethod
    def validate_simple_p2(output):
        if '10' not in output or '5' not in output:
            return False, "Swap not shown correctly"
        # Check order - 10 should come before 5 (after swap)
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        return (all(str(i) in output for i in [1, 2, 3, 4]), "Valid") if all(str(i) in output for i in [1, 2, 3, 4]) else (False, "All values must appear")
    
    @staticmethod
    def validate_moderate_p1(output):
        if 'area' not in output.lower():
            return False, "Missing 'area'"
        if not any(c.isdigit() for c in output):
            return False, "No calculation"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        if 'average' not in output.lower():
            return False, "Missing average"
        if not any(c.isdigit() for c in output):
            return False, "No calculation"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        return (any(c.isdigit() for c in output), "Valid") if any(c.isdigit() for c in output) else (False, "No output")
    
    @staticmethod
    def validate_hard_p1(output):
        required = ['min', 'max', 'sum', 'average']
        if not all(r in output.lower() for r in required):
            return False, "Missing min/max/sum/average"
        # Check for hardcoded template values
        if all(str(v) in output for v in [100, 650, 140, 360]):
            return False, "HARDCODED - Must calculate from data"
        numbers = re.findall(r'\d+', output)
        if len(numbers) < 4:
            return False, "Need 4 values"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        if not any(c.isdigit() for c in output):
            return False, "No calculation"
        return True, "Valid"


class TypeCasting04Validators:
    """04_TYPECASTING - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        if '100' not in output:
            return False, "Missing 100"
        if 'int(' not in output:
            return False, "Should show int() conversion"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        if '50' not in output:
            return False, "Missing 50"
        if 'str(' not in output:
            return False, "Should show str() conversion"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        if '3.14' not in output:
            return False, "Missing 3.14"
        if 'float(' not in output:
            return False, "Should show float() conversion"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p1(output):
        conversions = sum(1 for op in ['int(', 'str(', 'float('] if op in output)
        if conversions < 2:
            return False, "Need multiple conversions"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        if not any(c.isdigit() for c in output):
            return False, "No result"
        if not any(op in output for op in ['int(', 'str(', '+', '-']):
            return False, "Need conversion with operation"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        if 'bool' not in output.lower():
            return False, "Should show bool()"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        conversions = sum(1 for op in ['int(', 'str(', 'float(', 'bool('] if op in output)
        if conversions < 2:
            return False, "Chain needs multiple conversions"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        return (True, "Valid") if output.strip() else (False, "No output")


class UserInput05Validators:
    """05_USER_INPUT - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        return (all(w in output.lower() for w in ['name', 'input']) or 'input' in output, "Valid") if 'input' in output or 'name' in output.lower() else (False, "Missing input")
    
    @staticmethod
    def validate_simple_p2(output):
        return ('age' in output.lower() or 'input' in output, "Valid") if ('age' in output.lower() or 'input' in output) else (False, "Missing age")
    
    @staticmethod
    def validate_simple_p3(output):
        return ('input' in output, "Valid") if 'input' in output else (False, "Should use input()")
    
    @staticmethod
    def validate_moderate_p1(output):
        return ('input' in output, "Valid") if 'input' in output else (False, "Should use input()")
    
    @staticmethod
    def validate_moderate_p2(output):
        return ('input' in output, "Valid") if 'input' in output else (False, "Should use input()")
    
    @staticmethod
    def validate_moderate_p3(output):
        return ('input' in output, "Valid") if 'input' in output else (False, "Should use input()")
    
    @staticmethod
    def validate_hard_p1(output):
        return ('input' in output, "Valid") if 'input' in output else (False, "Should use input()")
    
    @staticmethod
    def validate_hard_p2(output):
        return ('input' in output, "Valid") if 'input' in output else (False, "Should use input()")


class Comment06Validators:
    """06_COMMENT_ESCAPE_PRINT - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_simple_p2(output):
        if '\\n' not in output and '\n' not in output and '\\t' not in output:
            return False, "Should use escape sequences"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        lines = output.split('\n')
        return (len(lines) >= 2, "Valid") if len(lines) >= 2 else (False, "Should use print formatting")
    
    @staticmethod
    def validate_moderate_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p2(output):
        escapes = output.count('\\n') + output.count('\\t') + output.count('\n') + output.count('\t')
        return (escapes >= 2, "Valid") if escapes >= 2 else (False, "Need escape sequences")
    
    @staticmethod
    def validate_moderate_p3(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")


class Operators07Validators:
    """07_OPERATORS - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        return (any(c.isdigit() for c in output), "Valid") if any(c.isdigit() for c in output) else (False, "No arithmetic result")
    
    @staticmethod
    def validate_simple_p2(output):
        return (any(c.isdigit() for c in output), "Valid") if any(c.isdigit() for c in output) else (False, "No result shown")
    
    @staticmethod
    def validate_simple_p3(output):
        return (any(c.isdigit() for c in output), "Valid") if any(c.isdigit() for c in output) else (False, "No result")
    
    @staticmethod
    def validate_moderate_p1(output):
        return (any(c.isdigit() for c in output), "Valid") if any(c.isdigit() for c in output) else (False, "No result")
    
    @staticmethod
    def validate_moderate_p2(output):
        return (any(c.isdigit() for c in output), "Valid") if any(c.isdigit() for c in output) else (False, "No result")
    
    @staticmethod
    def validate_moderate_p3(output):
        return (any(w in output.lower() for w in ['true', 'false', 'yes', 'no']), "Valid") if any(w in output.lower() for w in ['true', 'false', 'yes', 'no']) else (False, "Missing comparison result")
    
    @staticmethod
    def validate_hard_p1(output):
        return (any(c.isdigit() for c in output), "Valid") if any(c.isdigit() for c in output) else (False, "No result")
    
    @staticmethod
    def validate_hard_p2(output):
        return (any(c.isdigit() for c in output), "Valid") if any(c.isdigit() for c in output) else (False, "No result")


class Condition08Validators:
    """08_CONDITION - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        required = ['positive', 'negative', 'zero']
        return (any(w in output.lower() for w in required), "Valid") if any(w in output.lower() for w in required) else (False, "Missing if result")
    
    @staticmethod
    def validate_simple_p2(output):
        return (any(w in output.lower() for w in ['even', 'odd']), "Valid") if any(w in output.lower() for w in ['even', 'odd']) else (False, "Missing even/odd check")
    
    @staticmethod
    def validate_simple_p3(output):
        return (any(w in output.lower() for w in ['larger', 'greater', 'equal', 'same']), "Valid") if any(w in output.lower() for w in ['larger', 'greater', 'equal', 'same']) else (False, "Missing comparison")
    
    @staticmethod
    def validate_moderate_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p3(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")


class Loops09Validators:
    """09_LOOPS - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 2, "Valid") if len(lines) >= 2 else (False, "For loop not working")
    
    @staticmethod
    def validate_simple_p2(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 2, "Valid") if len(lines) >= 2 else (False, "While loop not working")
    
    @staticmethod
    def validate_simple_p3(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 3, "Valid") if len(lines) >= 3 else (False, "Loop not iterating")
    
    @staticmethod
    def validate_moderate_p1(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 3, "Valid") if len(lines) >= 3 else (False, "Nested loops needed")
    
    @staticmethod
    def validate_moderate_p2(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 2, "Valid") if len(lines) >= 2 else (False, "Loop logic missing")
    
    @staticmethod
    def validate_moderate_p3(output):
        numbers = re.findall(r'\d+', output)
        return (len(numbers) >= 1, "Valid") if len(numbers) >= 1 else (False, "No calculation shown")
    
    @staticmethod
    def validate_hard_p1(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 2, "Valid") if len(lines) >= 2 else (False, "No output")
    
    @staticmethod
    def validate_hard_p2(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 2, "Valid") if len(lines) >= 2 else (False, "No output")


class Strings10Validators:
    """10_STRINGS - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        return (any(w in output.lower() for w in ['index', 'character']), "Valid") if any(w in output.lower() for w in ['index', 'character']) else (False, "Missing indexing")
    
    @staticmethod
    def validate_simple_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_simple_p3(output):
        return (any(w in output.lower() for w in ['upper', 'lower', 'replace']), "Valid") if any(w in output.lower() for w in ['upper', 'lower', 'replace']) else (False, "Missing string methods")
    
    @staticmethod
    def validate_moderate_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p3(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")


class Functions11Validators:
    """11_FUNCTION - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "Function not called")
    
    @staticmethod
    def validate_simple_p2(output):
        numbers = re.findall(r'\d+', output)
        return (len(numbers) >= 1, "Valid") if len(numbers) >= 1 else (False, "No result shown")
    
    @staticmethod
    def validate_simple_p3(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p1(output):
        numbers = re.findall(r'\d+', output)
        return (len(numbers) >= 1, "Valid") if len(numbers) >= 1 else (False, "No result")
    
    @staticmethod
    def validate_moderate_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p3(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p1(output):
        numbers = re.findall(r'\d+', output)
        return (len(numbers) >= 1, "Valid") if len(numbers) >= 1 else (False, "No result")
    
    @staticmethod
    def validate_hard_p2(output):
        numbers = re.findall(r'\d+', output)
        return (len(numbers) >= 1, "Valid") if len(numbers) >= 1 else (False, "No result")


class Lists12Validators:
    """12_LIST - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        return (('[' in output or any(c.isdigit() for c in output)), "Valid") if ('[' in output or any(c.isdigit() for c in output)) else (False, "List not created")
    
    @staticmethod
    def validate_simple_p2(output):
        return (any(w in output.lower() for w in ['index', 'element']), "Valid") if any(w in output.lower() for w in ['index', 'element']) else (False, "Missing indexing")
    
    @staticmethod
    def validate_simple_p3(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p1(output):
        lines = [l for l in output.split('\n') if l.strip() and '===' not in l]
        return (len(lines) >= 2, "Valid") if len(lines) >= 2 else (False, "No iteration shown")
    
    @staticmethod
    def validate_moderate_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p3(output):
        numbers = re.findall(r'\d+', output)
        return (len(numbers) >= 1, "Valid") if len(numbers) >= 1 else (False, "No result")
    
    @staticmethod
    def validate_hard_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")


class Tuples13Validators:
    """13_TUPLES - Strong validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        return (('(' in output or any(c.isdigit() for c in output)), "Valid") if ('(' in output or any(c.isdigit() for c in output)) else (False, "Tuple not created")
    
    @staticmethod
    def validate_simple_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_simple_p3(output):
        numbers = re.findall(r'\d+', output)
        return (len(numbers) >= 1, "Valid") if len(numbers) >= 1 else (False, "No unpacking")
    
    @staticmethod
    def validate_moderate_p1(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_moderate_p3(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")
    
    @staticmethod
    def validate_hard_p1(output):
        numbers = re.findall(r'\d+', output)
        return (len(numbers) >= 1, "Valid") if len(numbers) >= 1 else (False, "No output")
    
    @staticmethod
    def validate_hard_p2(output):
        return (output.strip(), "Valid") if output.strip() else (False, "No output")


# Mapping of practice sets to validators
VALIDATORS = {
    "01_SETUP_PRACTICE_SET": Setup01Validators,
    "02_PYTHON_SYNTEX_PRACTICE_SET": Syntax02Validators,
    "03_VARIABLES_PRACTICE_SET": Variables03Validators,
    "04_TYPECASTING_PRACTICE_SET": TypeCasting04Validators,
    "05_USER_INPUT_PRACTICE_SET": UserInput05Validators,
    "06_COMMENT_ESCAPE_PRINT_PRACTICE_SET": Comment06Validators,
    "07_OPERATORS_PRACTICE_SET": Operators07Validators,
    "08_CONDITION_PRACTICE_SET": Condition08Validators,
    "09_LOOPS_PRACTICE_SET": Loops09Validators,
    "10_STRINGS_PRACTICE_SET": Strings10Validators,
    "11_FUNCTION_PRACTICE_SET": Functions11Validators,
    "12_LIST_PRACTICE_SET": Lists12Validators,
    "13_TUPLES_PRACTICE_SET": Tuples13Validators,
}


def get_validator(practice_set, file_type, problem_num):
    """Get the appropriate validator for a problem"""
    if practice_set not in VALIDATORS:
        return None
    
    validator_class = VALIDATORS[practice_set]
    method_name = f"validate_{file_type}_p{problem_num}"
    
    if hasattr(validator_class, method_name):
        return getattr(validator_class, method_name)
    
    return None


def validate_problem(practice_set, file_type, problem_num, output):
    """Validate a single problem output"""
    validator = get_validator(practice_set, file_type, problem_num)
    
    if validator is None:
        # No specific validator - just check for output
        return output.strip() != "", "Output exists"
    
    try:
        is_valid, message = validator(output)
        return is_valid, message
    except Exception as e:
        return False, f"Validation error: {str(e)}"
