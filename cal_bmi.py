def pounds_to_kg(pounds):
    """
    Convert pounds to kilograms.
    """
    return pounds * 0.453592

def inches_to_meters(inches):
    """
    Convert inches to meters.
    """
    return inches * 0.0254

def calculate_bmi(weight, height):
    """
    Calculate BMI using weight in kilograms and height in meters.
    Formula: BMI = weight(kg) / (height(m) ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value according to the standard BMI categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    get_name = input("Hello, what is your name? "). capitalize(). strip()
    print(f"Hi, {get_name}.", "Welcome to your BMI calculator!", end="\n\n")
    while True:
        try:
            need_explain = input("Would you like me to explain what BMI is? ").lower()
            if need_explain not in ["yes", "y", "no", "n",]:
                raise ValueError("Please enter 'yes' or 'no'.")
            a = """
        Body Mass Index (BMI) is a value derived from an individuals height and weight. 
        It is commonly used as a quick screening tool to assess whether someone has a healthy body
        relative to their height.

        Here are the ranges for BMI values:

        [Underweight]   0 - 18.4
        [Normal weight] 18.5 - 24.9
        [Overweight]    25 - 29.9
        [Obese]         30+

        Now, let's begin.
            """
            
            if need_explain in "yes":
                print(a, end="\n\n")
            elif need_explain == "y":
                print(a, end="\n\n")
            elif need_explain == "no":
                print("Great, let's get started.", end="\n\n")
            elif need_explain == "n":
                print("Great, let's get started.", end="\n\n")
            else:
                print("Great, let's get started.", end="\n\n")
            break  # Exit the loop if weight input is successful
        except ValueError as e:
            print("Oops, try again.", e)
    while True:
        try:
            system_choice = input("Do you prefer to enter your measurements in Imperial or Metric units? (type '1' for Imperial or '2' for Metric): ")
            if system_choice == '2':
                weight_unit = 'kg'
                height_unit = 'm'
                weight_prompt = "Enter your weight in kilograms: "
                height_prompt = "Enter your height in meters: "
                break
            elif system_choice == '1':
                weight_unit = 'lbs'
                height_unit = 'in'
                weight_prompt = "Enter your weight in pounds: "
                height_prompt = "Enter your height in inches: "
                break
            else:
                print("Oops, try again. Please enter '1' for Imperial or '2' for Metric.", end="\n\n")
        except ValueError as e:
            print("Oops, try again.", e)
    while True:
        try:
            weight = float(input(weight_prompt))
            height = float(input(height_prompt))

            if weight_unit == 'lbs':
                weight = pounds_to_kg(weight)  # Convert pounds to kilograms
                      
            if height_unit == 'in':
                height = inches_to_meters(height)  # Convert inches to meters
            break
        except ValueError:
            print("Oops, try again. Please enter numerical values for weight and height.", end="\n\n")
        
        
    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)
        
    print(f"{get_name}, your BMI is:", round(bmi, 2), [category], end="\n\n")

    if category == "Underweight":
        print(f"No worries, {get_name}! Looks like it's time to bulk up and make some gains!", end="\n\n")
    elif category == "Normal weight":
        print(f"Great job, {get_name}! Seems like you've got everything under control. Let's keep you on track!", end="\n\n")
    else:
        print(f"No worries, {get_name}! Looks like we've got some work to do. You'll hit your goals in no time.", end="\n\n")

if __name__ == "__main__":
    main()
