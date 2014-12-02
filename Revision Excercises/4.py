#Hugo
#Revision Excercise 4

def input_farenheit():
    farenheit = float(input("Please enter temperature in farenheit: "))
    return farenheit

def conversion(farenheit):
    celcius = (farenheit-32)*(5/9)
    return celcius

def return_celcius(celcius):
    celcius = conversion(farenheit)
    print("Your tempature is {0}degrees celcius".format(celcius))


farenheit = input_farenheit()
celcius = conversion(farenheit)
return_celcius(celcius)

