
# DASC 5300-002: Assignment 1

---

## Objective

The purpose of this assignment is to gain hands-on experience with Python programming, focusing on its application in data science. You will be working on tasks that cover Python topics related to:

- Conditional Execution
- Python Basics
- Data Structures in Python
- Iterations
- Comprehensions
- Functions
- Object-Oriented Programming (OOP) in Python
- File I/O

---

## Assignment Description

You will be working with a sales analysis dataset, which can be downloaded [here](https://www.kaggle.com/datasets/flenderson/sales-analysis).

### Task 1: Feature Selection (File: `feature_selection.py`)

1. **Data Science Thinking**: Before loading the dataset, identify up to 5 columns that you will remove and 2 columns that are most important. Provide a written justification explaining your choices.

### Task 2: Load Data and Save Filtered Dataset (File: `load_and_filter_data.py`)

1. **File I/O**: Load the raw sales analysis dataset from a CSV file. Remove the columns you identified in Task 1 and write the new dataset to a new CSV file.

### Task 3: Object Class for Product (File: `product.py`)

1. **OOP**: Create a Python class named `Product` in its own file. This class should have attributes relevant to the dataset (e.g., `SKU_number`, `SoldFlag`, `StrengthFactor`, etc.).
2. Add a constructor which takes a line of CSV data as input and parses it to initialize the attributes.

### Task 4: Data Management Class and Data Operations (File: `data_manager.py`)

1. **OOP**: Create a `DataManager` class in its own file with methods for the following:
    - Loading the filtered dataset from the new CSV file
    - Displaying data in a formatted table
    - Sorting data based on a column name (e.g., `StrengthFactor`)
    - Filtering data based on a given condition (e.g., products with `SoldFlag = 1`)

    **Note**: This should be done using raw python, not third-party libraries.

2. Test the `DataManager` class by loading the filtered dataset and displaying it in a formatted table in a script named `data_manager_test.py`. It should also demonstrate the sorting and filtering operations on at least one column.

### Task 5: Comprehensions (File: `list_comprehensions.py`)

1. Use list comprehensions to create a list of `SKU_numbers` for products with `StrengthFactor` greater than a given value.

### Task 6: Save and Load Data (File: `save_and_load_data.py`)

1. **File I/O**: Save the filtered and sorted data back to disk in JSON format using the `DataManager` class.
2. **File I/O**: Load and save the `Product` objects to disk using `pickle`.

---

## Guidelines

- Each class should be defined in its own file.
- Each task should be implemented in a separate script that can be run independently.
- Comment your code adequately to explain the logic behind it.
- Use functions to modularize your code.
- Handle exceptions where necessary to make your program robust.

---

## Submission

Please submit your Python code files, your written justification for feature selection, and any additional files you create during the assignment before the due date.

We will have download the data independently, so there is no need to upload it to the repo.
