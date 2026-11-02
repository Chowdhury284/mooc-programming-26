f= int(input('Please type in a temperature (F): '))
# converting into celsius formula= °C = (°F - 32) ÷ (9/5)
c= (f-32)/(9/5)
if c>=0:
    print (f"{f} degrees Fahrenheit equals {c} degrees Celsius")
if c<0:
    print (f"{f} degrees Fahrenheit equals {c} degrees Celsius")
    print ("Brr! It's cold in here!")