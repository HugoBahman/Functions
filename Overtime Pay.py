#Hugo
#Calculating Pay = Fuctions
#18/11/14

def work_details():
    hours = int(input("How many hours have you worked: "))
    pay = int(input("How much do you make an hour: "))
    return hours, pay
    
def calculate_basic_pay(hours,pay):
    total = hours*pay
    return total

def calculate_overtime_pay(hours,pay):
    overtime_hours = hours - 40
    total_overtime = overtime_hours * 1.5 * pay
    total_basic = 40 * pay
    total = total_overtime + total_basic
    return total

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def display_pay(total):
    print("You have made £{0}.".format(total))

def calculate_pay():
    hours, pay = work_details()
    total = calculate_total_pay(hours,pay)
    display_pay(total)

calculate_pay()




