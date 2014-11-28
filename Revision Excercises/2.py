#Revision Excercise 2
#Hugo

def input_number():
    number = int(input("Please enter an odd number: "))
    if number % 2 == 0:
        input_number()
    else:
        return number

def print_star(number):
    for count in range(number):
        count = number
        number = number - 2
        star = "*" * count
        print("{0:^{1}}".format(star,50))


number = input_number()
print_star(number)
