print("Welcome to the temperature converter!")
print("1 - Celsius\n2 - Fahrenheit\n3 - Kelvin")

unit1 = input("Select the temperature unit from: ")
unit2 = input("Select the temperature unit to convert to: ")


# Celcius
if unit1 == "1" and unit2 == "2":
    temp = float(input("Enter the temperature in Celsius: "))
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp}°F")

elif unit1 == "1" and unit2 == "3":
    temp = float(input("Enter the temperature in Celsius: "))
    converted_temp = temp + 273.15
    print(f"{temp}°C is equal to {converted_temp}K")

# Fahrenheit
elif unit1 == "2" and unit2 == "1":
    temp = float(input("Enter the temperature in Fahrenheit: "))
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted_temp}°C")

elif unit1 == "2" and unit2 == "3":
    temp = float(input("Enter the temperature in Fahrenheit: "))
    converted_temp = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F is equal to {converted_temp}K")

# Kelvin 
elif unit1 == "3" and unit2 == "1":
    temp = float(input("Enter the temperature in Kelvin: "))
    converted_temp = temp - 273.15
    print(f"{temp}K is equal to {converted_temp}°C")

elif unit1 == "3" and unit2 == "2":
    temp = float(input("Enter the temperature in Kelvin: "))
    converted_temp = (temp - 273.15) * 9/5 + 32
    print(f"{temp}K is equal to {converted_temp}°F")    

elif unit1 == unit2:
    print("You selected the same unit. No conversion needed.")

else:
    print("Invalid input. Please select a valid temperature unit.")