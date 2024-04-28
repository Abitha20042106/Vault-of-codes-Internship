import math

def convert_temperature(temp, unit):
    if unit == 'F':
        converted_temp = (temp - 32) * 5.0/9.0
        return round(converted_temp, 2)
    elif unit == 'C':
        converted_temp = (temp * 9.0/5.0) + 32
        return round(converted_temp, 2)
    else:
        raise ValueError("Invalid unit. Unit must be either 'F' or 'C'.")

# Example usage:
a=input("Enter 'F' or 'C'")
if a=='F':
    temp_f=int(input("Enter the fahrenheit"))
    temp_c = convert_temperature(temp_f, 'F')
    print(f"{temp_f} degrees Fahrenheit is equal to {temp_c} degrees Celsius.")
else:
    temp_c=int(input("Enter the Celcius"))
    temp_f = convert_temperature(temp_c, 'C')
    print(f"{temp_c} degrees Celsius is equal to {temp_f} degrees Fahrenheit.")
