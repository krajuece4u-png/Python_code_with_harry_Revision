# Two type of modules in Python
# 1. Built-in modules
# 2. External modules

# Example of built-in module: math
import math
print(math.sqrt(16))  # Output: 4.0

# list of all built-in modules:
# url = https://docs.python.org/3/py-modindex.html


# Example of external module: requests
import requests
response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200
# You may need to install the requests module using pip if not already installed:
# pip install requests