def calculate_bmi(weight, height, system):
    if system == "metric":
        bmi = weight / (height ** 2)
    else:
        bmi = (weight / (height ** 2)) * 703
    
    return bmi, None


def classify_category(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return category


def main():
    print("BMI Calculator")
    system = input("Enter the system of units (metric or imperial): ").lower()
    if("metric" in system):
        weight = float(input("Enter your weight in the kilograms: "))
        height = float(input("Enter your height in metres : "))
    elif("imperial" in system):
        weight = float(input("Enter your weight in the pounds: "))
        height = float(input("Enter your height in inches : "))
    else:
        print("Invalid system please choose metric or imperials")
        return
    bmi, error = calculate_bmi(weight, height, system)

    if error:
        print(error)
    else:
        category = classify_category(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

        if system == "metric":
            print(f"Weight: {weight} kg, Height: {height} meters")
        elif system == "imperial":
            print(f"Weight: {weight} pounds, Height: {height} inches")


if __name__ == "__main__":
    main()
