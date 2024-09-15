# Equation Parser and Evaluator

This Python program parses a mathematical equation, prompts the user to input values for the parameters, and evaluates the result. It allows users to input any mathematical equation using variables like `x`, `y`, `z`, and evaluates the equation based on user input.

## Features

- **Equation Parsing**: Automatically identifies variables from the equation.
- **User Input**: Asks for values of each variable in the equation.
- **Equation Evaluation**: Calculates the result using the input values.
  
## How to Run the Program

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/equation-parser.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd equation-parser
    ```
3. **Install the necessary dependencies** (if applicable):
    ```bash
    pip install -r requirements.txt
    ```
    - **Note**: No external dependencies are required for this program, so you can skip this step unless you've added extra libraries.
    
4. **Run the program**:
    ```bash
    python equation_parser.py
    ```

## Example Usage

```bash
Enter a mathematical equation (use parameters like x, y, z): x + 2 * y - z
Enter value for x: 5
Enter value for y: 3
Enter value for z: 1
The result of the equation 'x + 2 * y - z' with the given values is: 10.0
