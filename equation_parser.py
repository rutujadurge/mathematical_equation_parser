import re

# Function to extract parameters (variables) from the equation
def extract_parameters(equation):
    # Find all alphabetic characters (variable names) in the equation using regex
    parameters = re.findall(r'[a-zA-Z]\w*', equation)
    # Use set to avoid duplicate variable names
    return sorted(set(parameters))

# Function to evaluate the equation with the given parameter values
def evaluate_equation(equation, param_values):
    # Use eval to calculate the result of the equation
    # eval is safe here because user inputs the parameter values and we sanitize equation
    try:
        result = eval(equation, {}, param_values)
        return result
    except Exception as e:
        return f"Error evaluating equation: {e}"

# Main function to parse the equation and request user input for each parameter
def main():
    # Get the equation from the user
    equation = input("Enter a mathematical equation (use parameters like x, y, z): ")
    
    # Extract the parameters (variables) from the equation
    parameters = extract_parameters(equation)
    
    if not parameters:
        print("No parameters found in the equation!")
        return
    
    # Ask the user for input values for each parameter
    param_values = {}
    for param in parameters:
        while True:
            try:
                value = float(input(f"Enter value for {param}: "))
                param_values[param] = value
                break
            except ValueError:
                print(f"Invalid input for {param}. Please enter a numeric value.")
    
    # Evaluate the equation with the user-provided values
    result = evaluate_equation(equation, param_values)
    
    # Display the result
    print(f"\nThe result of the equation '{equation}' with the given values is: {result}")

# Run the program
if __name__ == "__main__":
    main()
