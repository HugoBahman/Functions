#Hugo
#Development Excercise 2

def get_number():
    number = int(input("Enter number: "))
    return number

def odd_check(number):
    if number % 2 == 0:
        print("That number is not odd")
    else:
        make_star(number)

def make_star(number):
    for count in range(1, number, 2):
        star = "*"
        print("{0}:^{1}".format(star, 50))
    for count in range(1, number, -2):
        star = "*"
        print("{0}:^{1}".format(star, 50))    
        
number = get_number()
odd_check(number)
