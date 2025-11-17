from datetime import datetime
from datetime import date

reason_list = ("annual service", "cosmetic repair", "mechanical repair - body", 
                "mechanical repair - wing", "mechanical repair - engine")

outcome_list = ("return to service", "further action(S) required", "grounded - do not fly")


def get_job_date():
    now = datetime.now()
    job_date = now.date()

    return job_date

def get_previous_date():
    
    flag = True
    
    while flag:
        user_date = input('Please enter date of the previous maintenance job (DD/MM/YYYY): ')

        try:
           datetime.strptime(user_date, "%d/%m/%Y").date()
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return datetime.strptime(user_date, "%d/%m/%Y").date()

def next_service_date():
    now = datetime.now()
    job_day = now.strftime("%d")
    job_month = now.strftime("%m")
    job_year = now.strftime("%Y")

    temp_year = int(job_month) + 1 

    next_date = str(job_day) + "/" + str(job_month) + "/" + int(temp_year) 

    return next_date


def cal_difference(prev, curr):
    prev_job = prev
    current_job = curr

    diff = current_job - prev_job

    return diff.days

def check_serial_num():
    flag = True
    
    while flag:
        print("###############################################")
        ser_num = input('Please enter the plane reference number: ')

        if len(ser_num) == 12: 
            flag = True
        else:    
            print('Serial number accepted!')
            flag = False
                
    return ser_num



def record_job_reason():
        
        print("")
        print("################################################")
        print("#### Please choose a reason for current job ####")
        print('## 1. Annual service')
        print("## 2. Cosmetic repair")
        print("## 3. Mechanical repair - body")
        print("## 4. Mechanical repair - wing")
        print("## 5. Mechanical repair - engine")        
        print("") 