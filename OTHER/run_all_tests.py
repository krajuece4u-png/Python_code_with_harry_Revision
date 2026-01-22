"""
Master Test Runner for Python Practice Sets
Run from the root directory to test all practice sets with percentage tracking
"""
import subprocess
import sys
import json
from pathlib import Path
import re

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

# Define practice set folders
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

def run_all_tests():
    """Run all test files and display verbose results with colors and percentage"""
    base_path = Path(__file__).parent
    
    total_passed = 0
    total_failed = 0
    total_tests = 0
    results = {}
    test_counter = 0
    
    for practice_set in PRACTICE_SETS:
        folder = base_path / practice_set
        if folder.exists():
            # Run tests with verbose output
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(folder), "-v", "--tb=no"],
                cwd=base_path,
                capture_output=True,
                text=True
            )
            
            output = result.stdout + result.stderr
            
            # Parse individual test results
            test_lines = [line for line in output.split('\n') if 'PASSED' in line or 'FAILED' in line]
            
            folder_passed = 0
            folder_failed = 0
            
            for line in test_lines:
                test_counter += 1
                
                # Extract test name and status
                if 'PASSED' in line:
                    folder_passed += 1
                    total_passed += 1
                    # Format: path/file.py::test_name PASSED
                    test_name = line.split('::')[1].split(' PASSED')[0] if '::' in line else 'test'
                    file_path = line.split('::')[0].strip() if '::' in line else 'unknown'
                    
                    # Calculate percentage
                    percentage = int((test_counter / 106) * 100)  # 106 total tests
                    
                    print(f"{file_path}::{test_name} {Colors.GREEN}PASSED{Colors.RESET} {Colors.CYAN}[{percentage}%]{Colors.RESET}")
                    
                elif 'FAILED' in line:
                    folder_failed += 1
                    total_failed += 1
                    test_name = line.split('::')[1].split(' FAILED')[0] if '::' in line else 'test'
                    file_path = line.split('::')[0].strip() if '::' in line else 'unknown'
                    
                    percentage = int((test_counter / 106) * 100)
                    print(f"{file_path}::{test_name} {Colors.RED}FAILED{Colors.RESET} {Colors.CYAN}[{percentage}%]{Colors.RESET}")
            
            total_tests += folder_passed + folder_failed
            results[practice_set] = {
                "passed": folder_passed,
                "failed": folder_failed,
                "total": folder_passed + folder_failed
            }
            
            # Print folder summary
            if folder_failed == 0 and folder_passed > 0:
                print(f"\n{Colors.CYAN}{'='*85}{Colors.RESET}")
                print(f"{Colors.GREEN}{folder_passed} passed{Colors.RESET} in {folder}")
                print(f"{Colors.CYAN}{'='*85}{Colors.RESET}\n")
            else:
                print(f"\n{Colors.CYAN}{'='*85}{Colors.RESET}")
                print(f"{Colors.GREEN}{folder_passed} passed{Colors.RESET}, {Colors.RED}{folder_failed} failed{Colors.RESET} in {folder}")
                print(f"{Colors.CYAN}{'='*85}{Colors.RESET}\n")
    
    # Print summary
    print(f"\n{Colors.CYAN}{'='*85}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}                            SUMMARY REPORT{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*85}{Colors.RESET}\n")
    
    print(f"{Colors.BOLD}{'Practice Set':<45} {'Passed':<12} {'Failed':<12} {'Status'}{Colors.RESET}")
    print(f"{Colors.CYAN}{'-'*85}{Colors.RESET}")
    
    for practice_set in PRACTICE_SETS:
        if practice_set in results:
            r = results[practice_set]
            if r["failed"] == 0:
                status = f"{Colors.GREEN}[PASS]{Colors.RESET}"
                passed_str = f"{Colors.GREEN}{r['passed']}{Colors.RESET}"
            else:
                status = f"{Colors.RED}[FAIL]{Colors.RESET}"
                passed_str = f"{Colors.YELLOW}{r['passed']}{Colors.RESET}"
            
            failed_str = f"{Colors.RED}{r['failed']}{Colors.RESET}" if r['failed'] > 0 else f"{Colors.GREEN}{r['failed']}{Colors.RESET}"
            print(f"{practice_set:<45} {passed_str:<20} {failed_str:<20} {status}")
    
    print(f"{Colors.CYAN}{'-'*85}{Colors.RESET}")
    passed_str = f"{Colors.GREEN}{total_passed}{Colors.RESET}"
    failed_str = f"{Colors.RED}{total_failed}{Colors.RESET}" if total_failed > 0 else f"{Colors.GREEN}{total_failed}{Colors.RESET}"
    print(f"{'TOTAL':<45} {passed_str:<20} {failed_str:<20}")
    
    # Calculate and display percentage
    if total_tests > 0:
        percentage = (total_passed / total_tests) * 100
        print(f"\n{Colors.CYAN}{'='*85}{Colors.RESET}")
        if percentage == 100:
            print(f"{Colors.GREEN}{Colors.BOLD}OVERALL SUCCESS RATE: {percentage:.1f}% ({total_passed}/{total_tests} tests passed){Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}{Colors.BOLD}OVERALL SUCCESS RATE: {percentage:.1f}% ({total_passed}/{total_tests} tests passed){Colors.RESET}")
        print(f"{Colors.CYAN}{'='*85}{Colors.RESET}\n")
        
        # Show progress bar
        bar_length = 50
        filled = int(bar_length * percentage / 100)
        bar = "=" * filled + " " * (bar_length - filled)
        print(f"Progress: {Colors.GREEN}[{bar}]{Colors.RESET} {percentage:.1f}%\n")
    else:
        print(f"\n{Colors.YELLOW}WARNING: No tests found!{Colors.RESET}")
    
    return total_passed, total_failed, total_tests

if __name__ == "__main__":
    print(f"\n{Colors.CYAN}{'='*85}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}   Running all Python Practice Set Tests...{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*85}{Colors.RESET}\n")
    
    passed, failed, total = run_all_tests()
    
    if failed == 0 and total > 0:
        print(f"{Colors.GREEN}{Colors.BOLD}CONGRATULATIONS! All tests passed!{Colors.RESET}\n")
        sys.exit(0)
    elif total == 0:
        print(f"{Colors.YELLOW}WARNING: No tests were run.{Colors.RESET}\n")
        sys.exit(1)
    else:
        print(f"{Colors.YELLOW}Keep working! {failed} tests still need to pass.{Colors.RESET}\n")
        sys.exit(1)
