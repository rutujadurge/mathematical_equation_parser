import re


def extract_parameters(equation):
    parameters = re.findall(r'[a-zA-Z]\w*', equation)
    return sorted(set(parameters))

def evaluate_equation(equation, param_values):
    try:
        result = eval(equation, {}, param_values)
        return result
    except Exception as e:
        return f"Error evaluating equation: {e}"

def main():
    equation = input("Enter a mathematical equation (use parameters like x, y, z): ")
    parameters = extract_parameters(equation)
    
    if not parameters:
        print("No parameters found in the equation!")
        return
    
    param_values = {}
    for param in parameters:
        while True:
            try:
                value = float(input(f"Enter value for {param}: "))
                param_values[param] = value
                break
            except ValueError:
                print(f"Invalid input for {param}. Please enter a numeric value.")
    
    result = evaluate_equation(equation, param_values)
    
    print(f"\nThe result of the equation '{equation}' with the given values is: {result}")

if __name__ == "__main__":
    main()
