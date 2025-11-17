'''
def menu():
    print("Function Menu:\nRectangle Area Calculator (RA1)\nTime Converter (TC2)\nBilling System (BS3)\nHospital Project (HP4)\nPassword Checker (PC5)")
    choice = str(input("Please input the Function you would like to access: "))
    if choice.lower() == "RA1":
        rectanglearea1()
    elif choice.lower() == "TC2":
        timeconverter2()
    elif choice.lower() == "BS3":
        billingsystem3()
    elif choice.lower() == "HP4":
        hospitalproject4()
    elif choice.lower() == "PC5":
        passwordchecker5()
    else:
        print("Invalid Choice")
        menu()
defmenu = str(input("Would you like to access the function menu? Y/N "))
if defmenu.lower == "y":
    menu()
'''