"""
Enhanced Test Runner - Tests that actually verify practice file solutions
This runner captures output from practice files and validates them
"""
import subprocess
import sys
from pathlib import Path
import io
from contextlib import redirect_stdout, redirect_stderr

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

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

FILE_TYPES = ["simple", "moderate", "hard"]

def run_practice_file(filepath):
    """Run a practice file and capture output"""
    try:
        result = subprocess.run(
            [sys.executable, str(filepath)],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        success = result.returncode == 0
        output = result.stdout
        error = result.stderr
        
        return success, output, error
    except subprocess.TimeoutExpired:
        return False, "", "Timeout - infinite loop detected"
    except Exception as e:
        return False, "", str(e)

def parse_problem_outputs(output):
    """Parse output to identify which individual problems have output"""
    problems = {}
    lines = output.split('\n')
    current_problem = None
    problem_output = []
    
    for line in lines:
        if 'PROBLEM' in line and '===' in line:
            # Save previous problem if exists
            if current_problem is not None and problem_output:
                problems[current_problem] = '\n'.join(problem_output).strip()
            
            # Extract problem number
            try:
                # Format: === PROBLEM X ===
                parts = line.split('PROBLEM')
                if len(parts) > 1:
                    prob_num = parts[1].strip().split()[0].strip('=').strip()
                    current_problem = f"PROBLEM {prob_num}"
                    problem_output = []
            except:
                pass
        elif current_problem is not None:
            if line.strip():  # Only collect non-empty lines
                problem_output.append(line)
    
    # Save last problem
    if current_problem is not None and problem_output:
        problems[current_problem] = '\n'.join(problem_output).strip()
    
    return problems

def check_solution_exists(filepath):
    """Check if practice file has actual solutions (not just TODO)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # If it has actual code beyond the template
    has_print_calls = content.count('print(') > 3  # More than just the problem headers
    has_string_literals = content.count('"') > 2 or content.count("'") > 2
    has_no_todo = 'TODO' not in content
    
    # Check for meaningful variable assignments or operations
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    meaningful_lines = 0
    
    for line in lines:
        # Skip comments, docstrings, problem headers
        if line.startswith('#') or '"""' in line or "'''" in line:
            continue
        # Skip print with === (problem headers)
        if 'print(' in line and '===' in line:
            continue
        # Count everything else
        if line and 'print(' in line:
            meaningful_lines += 1
        elif line and not line.startswith('"') and 'print' not in line:
            meaningful_lines += 1
    
    return meaningful_lines > 3 or (has_print_calls and has_no_todo)

def run_enhanced_tests():
    """Run enhanced tests on practice files"""
    base_path = Path(__file__).parent
    
    total_files = 0
    total_passed = 0
    total_failed = 0
    results = {}
    test_counter = 0
    
    print(f"\n{Colors.CYAN}{'='*90}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}   Enhanced Practice File Test Runner{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}   Testing Your Solutions{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*90}{Colors.RESET}\n")
    
    for practice_set in PRACTICE_SETS:
        folder = base_path / practice_set
        if not folder.exists():
            continue
        
        folder_passed = 0
        folder_failed = 0
        
        for file_type in FILE_TYPES:
            filepath = folder / f"{file_type}.py"
            total_files += 1
            
            if not filepath.exists():
                continue
            
            has_solution = check_solution_exists(filepath)
            
            if has_solution:
                # Try running it
                success, output, error = run_practice_file(filepath)
                test_counter += 1
                percentage = int((test_counter / 39) * 100)  # 39 total practice files
                
                if success:
                    folder_passed += 1
                    total_passed += 1
                    status = f"{Colors.GREEN}PASSED{Colors.RESET}"
                    print(f"{practice_set}/{file_type}.py {status} {Colors.CYAN}[{percentage}%]{Colors.RESET}")
                else:
                    folder_failed += 1
                    total_failed += 1
                    status = f"{Colors.RED}FAILED{Colors.RESET}"
                    print(f"{practice_set}/{file_type}.py {status} {Colors.CYAN}[{percentage}%]{Colors.RESET}")
                    if error:
                        error_line = error.split('\n')[0][:60]
                        print(f"  Error: {error_line}")
            else:
                test_counter += 1
                percentage = int((test_counter / 39) * 100)
                print(f"{practice_set}/{file_type}.py {Colors.YELLOW}[TODO]{Colors.RESET} {Colors.CYAN}[{percentage}%]{Colors.RESET}")
        
        # Folder summary
        if folder_passed > 0 or folder_failed > 0:
            print(f"\n{Colors.CYAN}{'='*90}{Colors.RESET}")
            if folder_failed == 0 and folder_passed > 0:
                print(f"{Colors.GREEN}{folder_passed} passed{Colors.RESET} in {folder}")
            else:
                print(f"{Colors.GREEN}{folder_passed} passed{Colors.RESET}, {Colors.RED}{folder_failed} failed{Colors.RESET} in {folder}")
            print(f"{Colors.CYAN}{'='*90}{Colors.RESET}\n")
        
        results[practice_set] = {
            "passed": folder_passed,
            "failed": folder_failed,
            "total": folder_passed + folder_failed
        }
    
    # Print detailed summary table
    print(f"\n{Colors.CYAN}{'='*90}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}                            SUMMARY REPORT{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*90}{Colors.RESET}\n")
    
    print(f"{Colors.BOLD}{'Practice Set':<45} {'Passed':<12} {'Status'}{Colors.RESET}")
    print(f"{Colors.CYAN}{'-'*90}{Colors.RESET}")
    
    for practice_set in PRACTICE_SETS:
        if practice_set in results:
            r = results[practice_set]
            if r["passed"] > 0:
                status = f"{Colors.GREEN}[SOLVED]{Colors.RESET}" if r["failed"] == 0 else f"{Colors.YELLOW}[PARTIAL]{Colors.RESET}"
                passed_str = f"{Colors.GREEN}{r['passed']}/3{Colors.RESET}"
            else:
                status = f"{Colors.YELLOW}[UNSOLVED]{Colors.RESET}"
                passed_str = f"{Colors.YELLOW}0/3{Colors.RESET}"
            
            print(f"{practice_set:<45} {passed_str:<20} {status}")
    
    print(f"{Colors.CYAN}{'-'*90}{Colors.RESET}")
    passed_str = f"{Colors.GREEN}{total_passed}{Colors.RESET}"
    failed_str = f"{Colors.RED}{total_failed}{Colors.RESET}" if total_failed > 0 else f"{Colors.GREEN}{total_failed}{Colors.RESET}"
    print(f"{'TOTAL':<45} {passed_str:<20}")
    
    # Calculate and display percentage
    if total_files > 0:
        total_tests = total_passed + total_failed + (39 - total_files + (39 - test_counter))
        if test_counter > 0:
            percentage = (total_passed / test_counter) * 100
        else:
            percentage = 0
        
        print(f"\n{Colors.CYAN}{'='*90}{Colors.RESET}")
        if percentage == 100 and total_passed > 0:
            print(f"{Colors.GREEN}{Colors.BOLD}OVERALL SUCCESS RATE: {percentage:.1f}% ({total_passed}/{test_counter} solutions passed){Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}{Colors.BOLD}OVERALL SUCCESS RATE: {percentage:.1f}% ({total_passed}/{test_counter} solutions passed){Colors.RESET}")
        print(f"{Colors.CYAN}{'='*90}{Colors.RESET}\n")
        
        # Show progress bar
        bar_length = 50
        filled = int(bar_length * percentage / 100)
        bar = "=" * filled + " " * (bar_length - filled)
        print(f"Progress: {Colors.GREEN}[{bar}]{Colors.RESET} {percentage:.1f}%\n")
    
    return total_passed, total_failed, test_counter

if __name__ == "__main__":
    print(f"\n{Colors.CYAN}{'='*90}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}   Running Practice File Tests...{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*90}{Colors.RESET}\n")
    
    passed, failed, total = run_enhanced_tests()
    
    if total == 0 or (passed == 0 and failed == 0):
        print(f"{Colors.YELLOW}{Colors.BOLD}No solutions written yet. Start solving!{Colors.RESET}\n")
        sys.exit(1)
    elif failed == 0 and passed == total:
        print(f"{Colors.GREEN}{Colors.BOLD}CONGRATULATIONS! All practice files have solutions and they all pass!{Colors.RESET}\n")
        sys.exit(0)
    elif passed > 0:
        print(f"{Colors.YELLOW}{Colors.BOLD}Great progress! Keep solving...{Colors.RESET}\n")
        sys.exit(0)
    else:
        print(f"{Colors.RED}{Colors.BOLD}Some solutions have errors. Debug and try again.{Colors.RESET}\n")
        sys.exit(1)
