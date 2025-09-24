# Renamed constants (check will fail because names are not exact)
F_TO_C = 5 / 9
C_TO_F = 9 / 5

# Renamed functions (check will fail)
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * F_TO_C

def to_fahrenheit(celsius):
    return (celsius * C_TO_F) + 32

def main():
    # Removed try-except block (check for ValueError handling will fail)
    
    # Removed user input, hardcoded values (user interaction check will fail)
    temp = 100
    unit = 'F'

    if unit == 'C':
        converted = to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    elif unit == 'F':
        converted = to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
