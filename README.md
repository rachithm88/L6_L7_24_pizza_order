# Lab 6 – Code and Branch Coverage Analysis

## Objective

The objective of this lab is to understand and implement code coverage and branch coverage testing using Python, pytest, and the coverage library.

The goal is to achieve at least 90% coverage by designing test cases for different conditions, decision branches, and boundary values.

## Application: Pizza Order System

The application contains three main functions:

1. **pizza_price():** Calculates pizza prices based on size, toppings, and cheese-burst selection.
2. **order_discount():** Calculates discounts based on order total, day of the week, and student status.
3. **delivery_status():** Determines delivery status based on delivery time and distance.

## Tools Used

- Python 3.13
- pytest
- coverage.py
- Visual Studio Code
- Git and GitHub

## Code Coverage Testing

**Test file:** `CodeCoverageTest_pizza_order_application.py`

The test cases cover valid and invalid pizza sizes, toppings, cheese-burst restrictions, discount conditions, and delivery statuses.

**Commands:**

`python -m coverage run --source=pizza_order -m pytest CodeCoverageTest_pizza_order_application.py`

`python -m coverage report -m`

**Verified results:**
- Tests Passed: 12/12
- Statements: 34
- Missed Statements: 0
- Code Coverage: **100%**

## Branch Coverage Testing

**Test file:** `BranchCoverageTest_pizza_order_application.py`

The test cases check true and false decision outcomes, exception handling, and boundary conditions, including delivery time limits and topping thresholds.

**Commands:**

`python -m coverage run --branch --source=pizza_order -m pytest BranchCoverageTest_pizza_order_application.py`

`python -m coverage report -m`

**Verified results:**
- Tests Passed: 19/19
- Statements: 34
- Missed Statements: 0
- Branches: 24
- Partially Covered Branches: 0
- Total Reported Coverage: **100%**

## Coverage Screenshots

### Code Coverage Result

![Code Coverage](code_coverage.png)

### Branch Coverage Result

![Branch Coverage](branch_coverage.png)

## Conclusion

The pizza-order application was tested using pytest and coverage.py. Additional test cases were created to exercise normal inputs, invalid inputs, boundary conditions, and alternative decision branches.

The tests achieved 100% reported code and branch coverage in local verification, exceeding the minimum 90% requirement.

Both test suites were designed without modifying the original application logic.
