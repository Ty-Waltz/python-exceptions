def convert(temp):
    f = temp
    c = ((temp - 32) * 5/9)
    return c


try:
    temp = int(input("Enter temperature in Fahrenhiet: "))
    celsius = convert(temp)
except ValueError:
    print("Please enter a number")
else:
    print(f"The {temp} in Celsius is: {celsius:.2f}")
finally:
    print("Thank you for your weather input!")

