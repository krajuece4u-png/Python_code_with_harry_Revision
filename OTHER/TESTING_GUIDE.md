# 🧪 Python Practice Sets - Testing Guide

## Overview
Each practice set folder now includes pytest test files to validate your solutions.

## Quick Start

### Install pytest (if not already installed)
```bash
pip install pytest
```

### Run Tests

#### 1. Run tests for a specific practice set:
```bash
cd 01_SETUP_PRACTICE_SET
pytest test_simple.py -v
pytest test_moderate.py -v
pytest test_hard.py -v
```

#### 2. Run all tests in a folder:
```bash
cd 01_SETUP_PRACTICE_SET
pytest . -v
```

#### 3. Run all tests for all practice sets:
```bash
# From the root directory
python run_all_tests.py
```

#### 4. Run tests with detailed output:
```bash
pytest test_simple.py -v --tb=short
pytest test_simple.py -v --tb=long  # More verbose
```

## File Structure

Each practice set folder contains:
- `simple.py` - 3 simple problems (with TODO comments)
- `test_simple.py` - Tests for simple problems
- `moderate.py` - 3 moderate problems (with TODO comments)
- `test_moderate.py` - Tests for moderate problems
- `hard.py` - 2 hard problems (with TODO comments)
- `test_hard.py` - Tests for hard problems

## How to Use Tests

### Step 1: Look at the test file
```bash
# Open the test file for reference
cat test_simple.py
```

### Step 2: Write your solution
Edit `simple.py`, `moderate.py`, or `hard.py` with your solutions

### Step 3: Run the tests
```bash
pytest test_simple.py -v
```

### Step 4: Check results
- ✅ `PASSED` - Your solution is correct!
- ❌ `FAILED` - Review your solution and try again

## Example Workflow

```bash
# 1. Navigate to a practice set
cd 03_VARIABLES_PRACTICE_SET

# 2. Edit the file with your solutions
nano simple.py

# 3. Run the tests
pytest test_simple.py -v

# 4. Review any failures and fix your code
# 5. Re-run the tests until all pass
```

## Pytest Commands Reference

| Command | Description |
|---------|------------|
| `pytest test_simple.py` | Run tests |
| `pytest test_simple.py -v` | Verbose output |
| `pytest test_simple.py -s` | Show print statements |
| `pytest test_simple.py -x` | Stop on first failure |
| `pytest test_simple.py -k function_name` | Run specific test |
| `pytest . --collect-only` | List all tests |
| `pytest . -q` | Quiet mode |

## Test Structure

Each test file contains functions that test specific problems:

```python
def test_problem_1_description():
    """Test problem 1"""
    # Arrange
    input_data = 10
    
    # Act
    result = some_function(input_data)
    
    # Assert
    assert result == expected_value
```

## Tips for Success

1. **Read the test first** - Understanding what the test expects helps you write correct solutions
2. **Follow the problem description** - Tests are based on problem requirements
3. **Run tests frequently** - Catch errors early
4. **Use -v flag** - Get detailed output about what passes/fails
5. **Check assertions** - Look at what the test expects vs. what you're getting

## Common Test Patterns

### Testing Functions
```python
def test_add_function():
    result = add(10, 20)
    assert result == 30
```

### Testing Lists
```python
def test_list_operations():
    nums = [1, 2, 3]
    assert len(nums) == 3
    assert nums[0] == 1
```

### Testing Strings
```python
def test_string_operations():
    text = "hello"
    assert len(text) == 5
    assert text.upper() == "HELLO"
```

### Testing Conditionals
```python
def test_conditional():
    result = get_grade(85)
    assert result == 'B'
```

## Troubleshooting

### "No tests ran"
- Ensure test files are named `test_*.py` or `*_test.py`
- Ensure functions are named `test_*`

### "Import Error"
- Make sure pytest is installed: `pip install pytest`
- Run from the correct directory

### "AssertionError"
- Your solution doesn't match expected output
- Check the test assertions to understand what's expected
- Review the problem description

## Next Steps

1. ✅ Complete all problems in each practice set
2. ✅ Run tests to verify your solutions
3. ✅ Review failing tests to understand requirements
4. ✅ Commit your solutions to git

---
**Happy Testing! 🚀**
