'''
Temperature Converter with Nested Functions and User Input:
Write a Python function called `temperature_converter` that takes a temperature value 
and a string representing the scale (‘C’ for Celsius or ‘F’ for Fahrenheit) as input. 
The function should convert the temperature from one scale to the other using nested functions 
and return the converted value.
'''

def temperature_converter(temp, scale):
    
    # Nested function to convert Celsius to Fahrenheit
    def c_to_f(c):
        return (c * 9/5) + 32
    
    # Nested function to convert Fahrenheit to Celsius
    def f_to_c(f):
        return (f - 32) * 5/9
    
    if scale.upper() == 'C':
        return c_to_f(temp)
    elif scale.upper() == 'F':
        return f_to_c(temp)
    else:
        return "Invalid scale! Please use 'C' or 'F'."

# Taking input from the user
temperature = float(input("Enter the temperature: "))
scale = input("Enter the scale (C/F): ")

# Call the function and print the result
converted_temp = temperature_converter(temperature, scale)
print(f"Converted Temperature: {converted_temp}")