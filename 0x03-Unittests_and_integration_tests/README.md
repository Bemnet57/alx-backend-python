# Access Nested Map - Unit Test

This project contains a unit test for the `access_nested_map` function defined in the `utils.py` module. This function is used to retrieve values from nested Python dictionaries using a sequence of keys (a path).

## 📂 File Structure

├── utils.py # Contains the access_nested_map function and other utilities
└── test_utils.py # Contains unit tests for access_nested_map using unittest


## 🧪 Description

The test suite is implemented using Python's built-in `unittest` module along with the `parameterized` library. It ensures that the `access_nested_map` function behaves correctly for multiple valid input scenarios.

## ✅ Tested Function

```python
access_nested_map(nested_map: Mapping, path: Sequence) -> Any


nested_map: A dictionary (can be deeply nested)

path: A sequence of keys representing the path to the desired value

Returns: The value found at the path location

🔍 Test Cases
The test suite verifies the following cases:

Input Nested Map	Path	Expected Output
{"a": 1}	("a",)	1
{"a": {"b": 2}}	("a",)	{"b": 2}
{"a": {"b": 2}}	("a", "b")	2

⚙️ How to Run the Tests
Make sure you have parameterized installed:

bash
Copy
Edit
pip install parameterized
Then run the test using:

bash
Copy
Edit
python3 -m unittest test_utils.py
📝 Requirements
Python 3.7

Code is formatted with pycodestyle

All functions and modules are properly documented

All files are executable and end with a new line

📄 License
This project is part of the ALX Software Engineering backend curriculum and is intended for educational purposes.