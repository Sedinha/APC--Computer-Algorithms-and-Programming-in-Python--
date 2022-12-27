T = input()

def fahrenheit(T):
    celsius = float(T)
    result = ((1.8 *(celsius)) + 32)
    print(f"Fahrenheit: {result:.2f}")

def kelvin(T):
    celsius = float(T)
    result = ((celsius) + 273.15)
    print(f"Kelvin: {result:.2f}")

fahrenheit(T)
kelvin(T)