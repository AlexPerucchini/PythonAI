
def f_to_c(f):
    fahrenheit = f
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def c_to_f(c):
    celsius = c
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

f = 45
celsius = round(f_to_c(f))
print(f"{f}°F is {celsius}°C")

c = 42
fahrenheit = round(c_to_f(c))
print(f"{c}°C is {fahrenheit}°F")
