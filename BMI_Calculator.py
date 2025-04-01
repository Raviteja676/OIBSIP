def get_input(prompt):
    """Function to get user input and ensure it's a valid float."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def calculate_bmi(weight, height):
    """Calculate and return the BMI rounded to 2 decimal places."""
    return round(weight / (height ** 2), 2)

def classify_bmi(bmi):
    """Classify BMI based on standard categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    
    weight = get_input("Enter your weight in kilograms: ")
    height = get_input("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    
    print(f"Your BMI is: {bmi}")
    print("Category:", category)
    print("For more detailed advice, please consult a healthcare professional.")

if _name_ == "_main_":
    main()
