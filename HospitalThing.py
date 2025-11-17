patients = {}
def menu():
    decision = int(input("What do you want to do?\n[1] Register Patients\n[2] View Patient Total\n[3] Reset Record\n[4] Exit\n"))
    if decision == 1:
        patientadditions = int(input("Enter the amount of patients you want to register: "))
        for _ in range (patientadditions):
            patientname = input("Enter name: ")
            patientage = input("Enter age: ")

        patients[_] = {
            "Name": patientname,
            "Age": patientage
        }
        print("Patients added successfully") # all of this is to input patient records
        menu()
        return patients
    elif decision == 2:
        print(patients) # gives the patients recorded
        menu()
        return patients
    elif decision == 3:
        print("wip") # don't know how to do this
    elif decision == 4:
        exit()
    else:
        print("Enter a valid value")
        menu()
menu()
'''
total_patients = 0

def add_patient(total_patients):
    total_patients
    total_patients += 1
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print("Patient added:", name)
    return total_patients

def view_total(total_patients):
    print("Total patients:", total_patients)
    return total_patients

def resetcount(total_patients):
    total_patients = 0
    print("record gone")
    view_total(total_patients)
'''