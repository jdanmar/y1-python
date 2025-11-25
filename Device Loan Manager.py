from time import sleep
loans = []
id = 1
def loancreate():
    global id
    print("Please create a new loan: \n\n")
    loan = {
        "Loan_ID: ": id,
        "Student_Name: ": input("Enter Student Name: "),
        "Student_ID: ": input("Enter Student ID: "),
        "Device: ": input("Enter the Device Type: "),
        "Device_ID: ": input("Enter the Device ID: "),
        "Date_Out: ": input("Enter the date it was given out: "),
        "Date_Due: ": input("Enter the date its due: "),
        "Returned? ": False
    }
    loans.append(loan)
    id += 1 # Creates a unique ID
    print("Loan Created!")
    sleep(2)
    return

def loanupdate():
    loanid = int(input("Enter the loan ID: "))
    for loan in loans:
        if loan["Loan_ID: "] == loanid: # Data validation
            choice = int(input("What do you want to do?\n[1] Mark as Returned\n[2] Update Due Date\n[3] Return to the Menu"))
            if choice == 1:
                loan["Returned? "] = True
                print("Successfully marked!\n\n")
                sleep(2)
            elif choice == 2:
                loan["Date Due: "] = input("Enter new due date: ")
                print("Date Due successfully updated!\n\n")
                sleep(2)
            elif choice == 3:
                deviceloanmanagermenu()
            return
    print("Loan ID not Found.")

def searchloan():
    loansearch = input("Enter the student ID or device ID: ")
    for loan in loans:
        if loan["Student_ID: "] or loan["Device_ID: "] == loansearch:
            print(loan)
        return
    print("Student/Device ID not Found.")

def viewloan():
    print("Loans:")
    if not loans: # Checks if there's any loans
        print("There are no current loans!")
        sleep(1.5)
        return
    for loan in loans:
        print(loan)

def deleteloan():
    loanidconfirmation = int(input("Enter loan ID: "))
    for loan in loans:
        if loan["Loan_ID: "] == loanidconfirmation:
            loan.clear()
            print("Loan deleted successfully!")
            sleep(2)
            return
    print("Loan ID not Found.")

def deviceloanmanagermenu():
    while True:
        print("Device Loan Manager")
        decision = int(input("[1] Create a loan\n[2] Update a loan\n[3] Search for a loan\n[4] View loans\n[5] Delete a loan\n[6] Exit\n> "))
        if decision == 1:
            loancreate()
        elif decision == 2:
            loanupdate()
        elif decision == 3:
            searchloan()
        elif decision == 4:
            viewloan()
        elif decision == 5:
            deleteloan()
        elif decision == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid value")
            deviceloanmanagermenu()
deviceloanmanagermenu()




