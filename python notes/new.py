def temperature(t):
    c=(t-32)*(5.0/9)
    return c
Fahrenheit=float(raw_input("enter the value of temperature in Fahrenheit:"))
celsius=temperature(Fahrenheit)
print celsius
