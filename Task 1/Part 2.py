#Bank Registration Function Task
#Hugo (Partner: Jordan)

def user_info():
    print("Please enter your details below: ")
    first_name = (input("First Name: ")
    last_name = input("Surname: ")
    gender = input("Gender: ")
    address = input("House No. and Street: ")
    town = input("Town: ")
    post_code = input("Post Code: ")
    return first_name, last_name, gender, address, town, post_code

def process_details (first_name, last_name, gender, address, town, post_code):
    if gender == "M" or gender == "m" or gender == "Male" or gender == "male":
        title = "Mr"
        return title
    elif gender  == "F" or gender == "f" or gender == "Female" or gender == "female":
        marital_status = input("Are you married: ")
        if marital_status == "Y" or marital_status == "y" or marital_status == "Yes" or marital_status == "yes":
            title = "Mrs"
            return title
        else:
            title = "Ms"
            return title

def return_message(title, first_name, last_name):
    print("Thank you {0}. {1} {2} for registering with our Online Bank. Registration is now complete.".format(title, first_name, last_name))


first_name, last_name, gender, address, town, post_code = user_info()
title = process_details(first_name, last_name, gender, address, town, post_code)
return_message(title, first_name, last_name)


