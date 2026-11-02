hourly_wage= float(input("Hourly wage: "))
hours_worked= float(input("Hours worked: "))
day= input("Day of the week: ")
if day!= "Sunday":
    print (f"Daily wages: {hourly_wage * hours_worked} euros")
if day== "Sunday":
    print (f"Daily wages: {2 * hourly_wage * hours_worked} euros")