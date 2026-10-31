number= int(input("How many times a week do you eat at the student cafeteria? "))
fprice= float(input("The price of a typical student lunch? "))
gspend= float(input("How much money do you spend on groceries in a week? "))
print()
daily= (fprice*number+gspend)/7
weekly= daily*7
print ("Average food expenditure:")
print (f"Daily: {daily} euros")
print (f"Weekly: {weekly} euros")
