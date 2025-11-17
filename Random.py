validation = True
name = input("What is your name?: ")
while validation:
    age = int(input("Enter your age: "))
    if age < 18:
        print("Unable to apply for a job. Please come back when you are older")
        validation = False
    elif age >= 18:
        print("Able to apply for a job")
        job = input("Do you have a job? Please reply with: Yes or No: ")
        if job == "no":
            print("You are not eglible for a loan")
        else:
            print("You are eglible for a loan")
            validation = False