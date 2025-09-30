# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_F = 32  # used for Fahrenheit offset

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F

# Main function
def main():
    try:
        temp_input = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        converted = convert_to_celsius(temp_input)
        print(f"{temp_input}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()
