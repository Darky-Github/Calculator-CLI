# CLI Calculator

A command-line calculator built with Python that supports **basic arithmetic operations** and **scientific functions**.

## Features
- Basic Operations: `+`, `-`, `*`, `/`, `**` (power), `%` (modulo)
- Scientific Functions: 
  - `sin`, `cos`, `tan` (Trigonometry, input in radians)
  - `log` (Base 10 logarithm)
  - `ln` (Natural logarithm)
  - `sqrt` (Square root)
  - `factorial` (Factorial of an integer)
  - `abs` (Absolute value)
  - `exp` (Exponential function)
  - `deg` (Convert radians to degrees)
  - `rad` (Convert degrees to radians)
- Infinite Input Handling: Process complex expressions like `5 + 4 * 2 - sin(3.14) / 2 + log(100)`.
- Error Handling: Catches and displays errors effectively.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/cli-calculator.git
```
2. Change into the program directory
```bash
cd cli-calculator
```
3. (OPTIONAL) 
Create a virtual environment for Linux users.
```
python3 -m venv venv
source venv/bin/activate
```
On Windows, use 
```
python3 -m venv venv
.\venv\Scripts\activate
```

4. Run the program
```
python3 main.py
```
