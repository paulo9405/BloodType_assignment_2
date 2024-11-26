# Blood Type Compatibility Checker

A simple Python program to check blood type compatibility for donors and recipients. The program also includes a menu-driven interface for easy use.

## Features

- Check which blood types can **donate** to a specific blood type.
- Check which blood types a specific blood type can **donate to**.
- Validates user inputs for blood type and menu options.

## Compatibility Table

| Blood Type | Can Donate To           | Can Receive From                  |
|------------|-------------------------|------------------------------------|
| A+         | A+, AB+                 | A+, A-, O+, O-                    |
| A-         | A+, A-, AB+, AB-        | A-, O-                            |
| B+         | B+, AB+                 | B+, B-, O+, O-                    |
| B-         | B+, B-, AB+, AB-        | B-, O-                            |
| AB+        | AB+                     | All Blood Types                   |
| AB-        | AB+, AB-                | AB-, A-, B-, O-                   |
| O+         | O+, A+, B+, AB+         | O+, O-                            |
| O-         | All Blood Types         | O-                                |

## Pre-requisites

- Python 3.x installed on your machine.
- Install the `termcolor` library by running: pip install termcolor


How to Run
1. Clone the repository: git clone https://github.com/paulo9405/BloodType_assignment_2.git

2. Navigate to the project directory

3. Run the program: python blood_type.py
   Run the tests: python tests.py

4. How to Use
Follow the menu options displayed on the terminal:

Option 1: Check who can donate to your blood type.
Option 2: Check who you can donate blood to.
Option 3: Exit the program.
Enter your blood type (e.g., A+, O-, AB+) when prompted.

View the results for donors or recipients.


## Example Output
[ =================================== ]
   Welcome to Blood Type Compatibility!
[ =================================== ]

Choose an option:
1. Check who can donate to your blood type.
2. Check who you can donate blood to.
3. Exit the program.

Enter your choice (1/2/3): 1
Enter your blood type (e.g., A+, O-, AB+): A+
Blood Type A+ can receive donations from: A+, A-, O+, O-



