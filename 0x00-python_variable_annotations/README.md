0x00. Python - Variable Annotations
Description
This project introduces variable annotations in Python 3. Using type hints, we can annotate function signatures and variables to enhance code clarity, improve developer tooling support, and assist with static type checkers like mypy.

Learning Objectives
By the end of this project, you should be able to:

Understand type annotations in Python 3.

Use type annotations to specify function signatures and variable types.

Apply the concept of duck typing in Python.

Validate your code using mypy.

Requirements
Python 3.7

Files interpreted/compiled on Ubuntu 18.04 LTS

All files should end with a new line

Files must be executable and use #!/usr/bin/env python3 as the first line

Code should follow pycodestyle (version 2.5)

All modules, functions, and classes must be properly documented with meaningful docstrings

A README.md file is mandatory

Project Structure
Each task involves implementing a specific function using type annotations:

Mandatory Tasks

File	Task	Description
0-add.py	0	Type-annotated function add that returns the sum of two floats
1-concat.py	1	Type-annotated function concat that returns a concatenated string
2-floor.py	2	Type-annotated function floor that returns the floor of a float
3-to_str.py	3	Type-annotated function to_str that returns the string representation of a float
4-define_variables.py	4	Define and annotate variables: a, pi, i_understand_annotations, school
5-sum_list.py	5	Type-annotated function sum_list that returns the sum of a list of floats
6-sum_mixed_list.py	6	Type-annotated function sum_mixed_list that returns the sum of a list of ints and floats
7-to_kv.py	7	Type-annotated function to_kv that returns a tuple of a string and a squared number (as float)
8-make_multiplier.py	8	Type-annotated function make_multiplier that returns a function multiplying a float by a multiplier
Usage
bash
Copy
Edit
./0-main.py
./1-main.py
...
./8-main.py
Each file has a corresponding main test script (X-main.py) for local testing.

Resources
Python 3 Typing Documentation

MyPy Cheat Sheet
