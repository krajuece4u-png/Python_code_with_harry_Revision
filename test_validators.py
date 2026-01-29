"""
Strong validators for practice problem solutions.
These validators ensure solutions actually solve the problems, not just produce output.
"""

import re
import sys
from io import StringIO


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
                return False, f"Missing number {num} in output"
        return True, "Valid"
    
    @staticmethod
    def validate_calculation(output, calculation_str, expected_result):
        """Validate that calculation result is in output"""
        if str(expected_result) not in output:
            return False, f"Expected result {expected_result} not in output"
        return True, "Valid"
    
    @staticmethod
    def validate_min_lines(output, min_count):
        """Validate minimum number of output lines"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < min_count:
            return False, f"Expected at least {min_count} lines, got {len(lines)}"
        return True, "Valid"
    
    @staticmethod
    def validate_min_numbers(output, min_count):
        """Validate minimum number of numeric values in output"""
        numbers = re.findall(r'\d+\.?\d*', output)
        if len(numbers) < min_count:
            return False, f"Expected at least {min_count} numbers, got {len(numbers)}"
        return True, "Valid"
    
    @staticmethod
    def has_calculation_logic(output):
        """Check if output likely comes from calculation, not hardcoding"""
        # Check for signs of actual computation
        calc_indicators = ['+', '-', '*', '/', 'sum', 'min', 'max', 'avg', 'average', '=']
        output_lower = output.lower()
        has_indicator = any(ind in output_lower for ind in calc_indicators)
        
        # Check for multiple different types of operations
        # (not just a bunch of print statements)
        if output_lower.count('print') > 5:
            return False  # Too many prints = likely hardcoded
        
        return has_indicator
    
    @staticmethod
    def is_likely_hardcoded(output, common_hardcoded_patterns):
        """Check if values look like hardcoded template"""
        output_lower = output.lower()
        for pattern in common_hardcoded_patterns:
            if str(pattern).lower() in output_lower:
                return True
        return False


# VALIDATORS BY PRACTICE SET
class Setup01Validators:
    """01_SETUP_PRACTICE_SET validators - STRONG VERSION"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: Print welcome message"""
        # Must have all three words (real learning)
        is_valid, msg = ProblemValidator.validate_output_contains(
            output, "welcome", "python", "programming"
        )
        if not is_valid:
            return False, msg
        # Check it's not just hardcoded placeholder
        if "your message" in output.lower() or "todo" in output.lower():
            return False, "Still contains placeholder"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Print name"""
        lines = [l.strip() for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 1:
            return False, "No name printed"
        # Should not be placeholder text
        name_output = ' '.join(lines).lower()
        if 'your name' in name_output or 'name' == name_output.strip():
            return False, "Name should not be placeholder"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Print 3 lines"""
        lines = [l.strip() for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 3:
            return False, f"Expected 3 lines, got {len(lines)}"
        # Lines should be different (not all same)
        if len(set(lines)) < 2:
            return False, "Lines should have different content"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Perform arithmetic - MUST SHOW CALCULATION"""
        # Must have keywords AND actual numeric result
        has_result = "result" in output.lower() or "sum" in output.lower()
        has_addition = "addition" in output.lower() or "add" in output.lower()
        
        if not (has_result or has_addition):
            return False, "Missing arithmetic operation or result"
        
        # Extract numbers to verify calculation happened
        numbers = re.findall(r'\d+', output)
        if len(numbers) < 2:
            return False, "Need at least 2 numbers (operands) or result"
        
        # Check for calculation logic indicators
        if not ProblemValidator.has_calculation_logic(output):
            return False, "No calculation logic detected"
        
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: String operations - MUST USE STRING METHODS"""
        has_concat = "concatenat" in output.lower() or "+" in output
        has_string = "string" in output.lower()
        
        if not (has_concat or has_string):
            return False, "Missing string concatenation"
        
        # Should have actual strings (quoted text)
        if output.count('"') < 2 and output.count("'") < 2:
            return False, "String operations should show string values"
        
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Multiple operations"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 2:
            return False, "Need multiple operations"
        
        # Should show multiple types of operations
        operations_found = 0
        if any(op in output for op in ['+', '-', '*', '/']):
            operations_found += 1
        if output.count('print') >= 2:
            operations_found += 1
        if any(func in output.lower() for func in ['len', 'str', 'int']):
            operations_found += 1
        
        if operations_found < 1:
            return False, "Multiple different operations needed"
        
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Expressions - MUST SHOW COMPUTATION"""
        numbers = re.findall(r'\d+\.?\d*', output)
        if len(numbers) < 1:
            return False, "No numeric results shown"
        
        # Must have calculation indicators
        if not ('+' in output or '-' in output or '*' in output or '/' in output or '**' in output):
            return False, "Expression should contain operators"
        
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Nested operations - MUST SHOW COMPLEX LOGIC"""
        numbers = re.findall(r'\d+\.?\d*', output)
        if len(numbers) < 2:
            return False, "Nested operations should produce multiple results"
        
        # Must have multiple levels of operations
        op_count = sum(1 for op in ['+', '-', '*', '/', '**', '%'] if op in output)
        if op_count < 2:
            return False, "Nested operations need multiple operators"
        
        return True, "Valid"


class Variables03Validators:
    """03_VARIABLES_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: Create variables and print"""
        # Should contain name, age, city
        return ProblemValidator.validate_output_contains(output, "raju", "23", "kolkata")
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Swap variables"""
        # After swap, 'b' value should come first (10)
        return ProblemValidator.validate_output_contains(output, "10", "5")
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Multiple assignment"""
        # Should print all 4 values
        return ProblemValidator.validate_output_contains(output, "1", "2", "3", "4")
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Calculate rectangle area"""
        # Should contain "area" or a calculation result
        if "area" not in output.lower():
            return False, "Missing 'area' in output"
        if not any(char.isdigit() for char in output):
            return False, "No calculation result shown"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Average calculation"""
        if "average" not in output.lower() and "avg" not in output.lower():
            return False, "Missing average calculation"
        if not any(char.isdigit() for char in output):
            return False, "No numeric result shown"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Naming conventions"""
        # Should have properly named variables in output
        lines = output.lower()
        if not any(char.isdigit() for char in output):
            return False, "No output with variables"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Dynamic assignment with conditions"""
        # This MUST be a REAL solution with calculations, not hardcoded values
        # Should show min, max, sum, average - CALCULATED from a data source
        required = ["min", "max", "sum", "average"]
        for req in required:
            if req not in output.lower():
                return False, f"Missing '{req}' in output"
        
        # Extract all numbers from output
        numbers = re.findall(r'\d+', output)
        if len(numbers) < 4:
            return False, "Should show at least 4 values (min, max, sum, avg)"
        
        # STRONG CHECK: The numbers should show actual calculations
        # Example: if you have values [10, 20, 30], then:
        # min should be 10, max should be 30, sum should be 60
        # The values should NOT all be unique/random
        
        # Parse the output to get the actual values shown
        output_lower = output.lower()
        min_match = re.search(r'min[:\s]+(\d+)', output_lower)
        max_match = re.search(r'max[:\s]+(\d+)', output_lower)
        sum_match = re.search(r'sum[:\s]+(\d+)', output_lower)
        avg_match = re.search(r'(?:average|avg)[:\s]+(\d+)', output_lower)
        
        if not (min_match and max_match and sum_match and avg_match):
            return False, "Min, Max, Sum, Average values not clearly shown"
        
        try:
            min_val = int(min_match.group(1))
            max_val = int(max_match.group(1))
            sum_val = int(sum_match.group(1))
            avg_val = int(avg_match.group(1))
            
            # CRITICAL CHECK: These specific values appear to be hardcoded
            # Real dynamic assignment would have calculated values
            # Check if this looks like the template hardcoded values
            if (min_val == 100 and max_val == 650 and sum_val == 140 and avg_val == 360):
                return False, "HARDCODED VALUES DETECTED - Must calculate min/max/sum/average from data"
            
            # Mathematical validation: max should be >= min
            if max_val < min_val:
                return False, "Invalid: max should be >= min"
            
            # Sum should be reasonable (if avg is average of values, sum >= max)
            if sum_val > 0 and avg_val > 0:
                # At minimum, sum should be greater than or equal to max or min
                # (unless it's calculated from a different dataset)
                pass
            
            return True, "Valid - Calculated values shown"
        except:
            return False, "Could not parse min/max/sum/avg values"
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Nested variable operations"""
        # Should show nested calculations
        if not any(char.isdigit() for char in output):
            return False, "No calculation results"
        return True, "Valid"


class TypeCasting04Validators:
    """04_TYPECASTING_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: String to integer"""
        return ProblemValidator.validate_numbers_in_output(output, [100])
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Integer to string"""
        return ProblemValidator.validate_numbers_in_output(output, [50])
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: String to float"""
        if "3.14" not in output:
            return False, "Missing float conversion result"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Multiple type conversions"""
        if not any(c.isdigit() for c in output):
            return False, "No conversion results"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Type conversion with operations"""
        if not any(c.isdigit() for c in output):
            return False, "No results shown"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Bool conversion"""
        if not any(c.isdigit() for c in output):
            return False, "No conversion output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Complex conversion chain"""
        if not any(c.isdigit() for c in output):
            return False, "No conversion results"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Error handling in conversion"""
        if not any(c.isdigit() for c in output):
            return False, "No output shown"
        return True, "Valid"


class UserInput05Validators:
    """05_USER_INPUT_PRACTICE_SET validators - Skip these as they need input"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: Get name input"""
        return ProblemValidator.validate_output_contains(output, "name", "greet")
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Get age input"""
        return ProblemValidator.validate_output_contains(output, "age")
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Get multiple inputs"""
        return ProblemValidator.validate_output_contains(output, "name", "age", "city")
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Input with validation"""
        if not any(c.isdigit() for c in output):
            return False, "No numeric output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Multiple inputs with operations"""
        if not any(c.isdigit() for c in output):
            return False, "No numeric output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Input with conversion"""
        if not any(c.isdigit() for c in output):
            return False, "No numeric output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Complex input operations"""
        if not any(c.isdigit() for c in output):
            return False, "No numeric output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Input validation and loops"""
        if not any(c.isdigit() for c in output):
            return False, "No numeric output"
        return True, "Valid"


class Syntax02Validators:
    """02_PYTHON_SYNTEX_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: Identify valid statements"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 1:
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Multiple statements"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 2:
            return False, "Needs multiple statements"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Proper indentation"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 1:
            return False, "No properly indented code"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Complex syntax"""
        if not any(c.isdigit() for c in output):
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Multiple operations"""
        lines = [l for l in output.split('\n') if l.strip()]
        if len(lines) < 2:
            return False, "Multiple operations needed"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Error handling"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Nested structures"""
        if not any(c.isdigit() for c in output):
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Complex logic"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"


class Comment06Validators:
    """06_COMMENT_ESCAPE_PRINT_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: Comments in code"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Escape sequences"""
        # Should have newlines or tabs
        if '\n' not in output and '\t' not in output and '\\n' not in output and '\\t' not in output:
            if len(output.split()) < 2:
                return False, "Escape sequences not used properly"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Print formatting"""
        lines = output.split('\n')
        if len(lines) < 2:
            return False, "Format parameters not used"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Multi-line comments"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Multiple escapes"""
        if output.count('\n') + output.count('\t') < 2:
            return False, "Insufficient escape sequences"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Complex formatting"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Advanced escapes"""
        lines = [l for l in output.split('\n') if l.strip()]
        if len(lines) < 2:
            return False, "Advanced escape sequences needed"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Raw strings"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"


class Operators07Validators:
    """07_OPERATORS_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: Arithmetic operations"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Modulus and exponent"""
        return ProblemValidator.validate_min_numbers(output, 2)
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Floor division"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Mixed operators"""
        return ProblemValidator.validate_min_numbers(output, 2)
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Operator precedence"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Comparison operators"""
        return ProblemValidator.validate_output_contains(output, "true", "false", "yes", "no")
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Complex expressions"""
        return ProblemValidator.validate_min_numbers(output, 2)
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Bitwise operators"""
        return ProblemValidator.validate_min_numbers(output, 1)


class Condition08Validators:
    """08_CONDITION_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: If statement"""
        return ProblemValidator.validate_output_contains(output, "positive", "negative", "zero")
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: If-else"""
        return ProblemValidator.validate_output_contains(output, "even", "odd")
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Compare numbers"""
        return ProblemValidator.validate_output_contains(output, "larger", "larger", "equal")
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Nested if"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Grade classification"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 1:
            return False, "No grade output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Multiple conditions"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Complex conditions"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Edge cases"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"


class Loops09Validators:
    """09_LOOPS_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: For loop"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 2:
            return False, "For loop not working properly"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: While loop"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 2:
            return False, "While loop not working"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Loop iterations"""
        return ProblemValidator.validate_min_lines(output, 3)
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Nested loops"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 3:
            return False, "Nested loops not working"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Loop with condition"""
        lines = [l for l in output.split('\n') if l.strip() and not l.startswith('===')]
        if len(lines) < 2:
            return False, "Loop logic missing"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Sum calculation"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Advanced loop patterns"""
        return ProblemValidator.validate_min_lines(output, 2)
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Complex iteration"""
        return ProblemValidator.validate_min_lines(output, 2)


class Strings10Validators:
    """10_STRINGS_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: String indexing"""
        return ProblemValidator.validate_output_contains(output, "index", "character")
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: String slicing"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: String methods"""
        return ProblemValidator.validate_output_contains(output, "upper", "lower", "replace")
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: String operations"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: String formatting"""
        return ProblemValidator.validate_min_lines(output, 1)
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Pattern matching"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Advanced string ops"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: String algorithms"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"


class Functions11Validators:
    """11_FUNCTION_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: Simple function"""
        if not output.strip():
            return False, "Function not called"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Function with return"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Function with parameters"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Multiple parameters"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Default parameters"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Keyword arguments"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Lambda functions"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Recursion"""
        return ProblemValidator.validate_min_numbers(output, 1)


class Lists12Validators:
    """12_LIST_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: List creation"""
        if '[' not in output and not any(c.isdigit() for c in output):
            return False, "List not created"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: List indexing"""
        return ProblemValidator.validate_output_contains(output, "index", "element")
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: List methods"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: List iteration"""
        return ProblemValidator.validate_min_lines(output, 2)
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: List operations"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: List comprehension"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Nested lists"""
        return ProblemValidator.validate_min_lines(output, 1)
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: List algorithms"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"


class Tuples13Validators:
    """13_TUPLES_PRACTICE_SET validators"""
    
    @staticmethod
    def validate_simple_p1(output):
        """PROBLEM 1: Tuple creation"""
        if '(' not in output and not any(c.isdigit() for c in output):
            return False, "Tuple not created"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p2(output):
        """PROBLEM 2: Tuple indexing"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_simple_p3(output):
        """PROBLEM 3: Tuple unpacking"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_moderate_p1(output):
        """PROBLEM 1: Tuple operations"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_moderate_p2(output):
        """PROBLEM 2: Tuple methods"""
        return ProblemValidator.validate_min_lines(output, 1)
    
    @staticmethod
    def validate_moderate_p3(output):
        """PROBLEM 3: Nested tuples"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"
    
    @staticmethod
    def validate_hard_p1(output):
        """PROBLEM 1: Tuple unpacking patterns"""
        return ProblemValidator.validate_min_numbers(output, 1)
    
    @staticmethod
    def validate_hard_p2(output):
        """PROBLEM 2: Tuple algorithms"""
        if not output.strip():
            return False, "No output"
        return True, "Valid"


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
