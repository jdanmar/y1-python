hourspernight = input("How many hours per night do you sleep? ")
hoursperweek = 7*int(hourspernight)
print("You sleep", hoursperweek,"hours per week")
hourspermonth = float(hoursperweek)*4.35
print("You sleep", hourspermonth, "hours per month")

dayspermonth = float(hourspermonth)/24
print("This equates to", dayspermonth, "days per month")


username = input("What is your name? ")
mpnetwork = input("What is your mobile phone network? ")
nofminutes = int(input("How many minutes have you used this month? "))
monthlyminutes = nofminutes*0.10
noftexts = int(input("How many texts have you sent in a month? "))
monthlytexts = noftexts*0.05
monthlytotal = monthlytexts + monthlyminutes
print("Your monthly total is: £",monthlytotal)
VATtotal = monthlytotal/0.2
print("Your monthly total with VAT is: £",VATtotal)
