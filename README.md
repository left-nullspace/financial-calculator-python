# Financial Calculator Python

This is an interactive financial calculator implemented in Python. It allows users to perform various interest calculations, including simple interest, compound interest, periodic interest, continuous interest, and interest with periodic deposits. Users can input the required parameters and receive immediate results for their financial calculations.

## Features

- Interactive console-based user interface
- Calculation of different types of interest:
  - Simple Interest
  - Compound Interest
  - Periodic Interest
  - Continuous Interest
  - Interest with Periodic Deposits
- Easy-to-follow prompts and detailed explanations for each calculation
- Modular code structure for better organization and maintenance

## How It Works

1. **Main Menu**: The user is presented with a menu of different financial formulas to choose from.
2. **User Input**: After selecting a formula, the user is prompted to enter the necessary parameters.
3. **Calculation**: The program performs the calculation based on the user's input and displays the result.
4. **Repeat or Exit**: The user is asked if they want to perform another calculation or exit the program.

## Project Structure

- `financial_calculations.py`: Contains all the calculation methods for the different types of interest.
- `menu.py`: Handles the user interactions, displays the menu, and processes the user's choices.
- `main.py`: The entry point of the program, manages the main loop for user interaction.

## Usage

To run the program, execute the `main.py` file. Follow the prompts to perform your desired financial calculations.

### Example Interaction

```
Which formula would you like to use?
1. Simple Interest Future Value (FV)
2. Simple Interest Present Value (PV) 
3. Simple Interest Rate (r) 
4. Compound Interest Future Value (FV) 
5. Compound Interest Present Value (PV) 
6. Compound Interest Rate (r)
7. Periodic Interest Future Value (FV)
8. Periodic Interest Present Value (PV) 
9. Periodic Interest Rate (r) 
10. Continuous Interest Future Value (FV) 
11. Continuous Interest Present Value (PV) 
12. Continuous Interest Rate (r)
13. Interest with Periodic Deposit Future Value (FV) 
user: 1
Recall: PV = Present Value, r = Interest Rate, n = Number of Periods
Enter PV, r, n separated by spaces:
user: 1000 0.05 50
Future Value: 3500.0
You will have 3500.0 in 50 years with a simple interest rate of 5.0%.
Do you want to perform another calculation? (yes/no)
user: no
```

## Formulas

### Simple Interest

#### 1. Future Value (FV)
$$
FV = (1 + r \cdot n) \cdot PV
$$
- `PV` = Present Value
- `r` = Interest Rate
- `n` = Number of Periods

#### 2. Present Value (PV)
$$
PV = \frac{FV}{1 + r \cdot n}
$$

#### 3. Interest Rate (r)
$$
r = \frac{FV}{PV} - 1
$$

### Compound Interest

#### 4. Future Value (FV)
$$
FV = PV \cdot (1 + r)^n
$$
- `PV` = Present Value
- `r` = Interest Rate
- `n` = Number of Periods

#### 5. Present Value (PV)
$$
PV = \frac{FV}{(1 + r)^n}
$$

#### 6. Interest Rate (r)
$$
r = \left( \frac{FV}{PV} \right)^{\frac{1}{n}} - 1
$$

### Periodic Interest

#### 7. Future Value (FV)
$$
FV = PV \cdot \left(1 + \frac{r}{m}\right)^{m \cdot n}
$$
- `PV` = Present Value
- `r` = Interest Rate
- `n` = Number of Periods
- `m` = Number of Compounding Periods per Year

#### 8. Present Value (PV)
$$
PV = \frac{FV}{\left(1 + \frac{r}{m}\right)^{m \cdot n}}
$$

#### 9. Interest Rate (r)
$$
r = \left( \frac{FV}{PV} \right)^{\frac{1}{m \cdot n}} - 1
$$
$$
r = r \cdot m
$$

### Continuous Interest

#### 10. Future Value (FV)
$$
FV = PV \cdot e^{r \cdot n}
$$
- `PV` = Present Value
- `r` = Interest Rate
- `n` = Number of Periods

#### 11. Present Value (PV)
$$
PV = \frac{FV}{e^{r \cdot n}}
$$

#### 12. Interest Rate (r)
$$
r = \frac{\ln(FV / PV)}{n}
$$
- `ln` = Natural Logarithm

### Interest with Periodic Deposit

#### 13. Future Value (FV)
$$
FV = \frac{A}{\frac{r}{m}} \cdot \left( \left(1 + \frac{r}{m}\right)^{m \cdot n} - 1 \right)
$$
- `A` = Amount Deposited Periodically
- `r` = Interest Rate
- `n` = Number of Periods
- `m` = Number of Compounding Periods per Year

#### Present Value (PV)
$$
PV = \frac{A}{\frac{r}{m}} \cdot \left( 1 - \frac{1}{\left(1 + \frac{r}{m}\right)^{m \cdot n}} \right)
$$

## Running the Program

Ensure all files (`financial_calculations.py`, `menu.py`, and `main.py`) are in the same directory or appropriately referenced in your project structure. Execute the `main.py` file:

```sh
python main.py
```

This project provides a clear and interactive way to perform various financial calculations, making it a useful tool for anyone interested in financial mathematics.
