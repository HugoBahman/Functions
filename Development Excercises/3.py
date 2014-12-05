#Hugo
#Development Excercise 3

def get_currencies():
    fc = input("£, $, €: ")
    amount = float(input("How much are you converting: "))
    sc = input("£, $, €: ")
    return fc, sc, amount

def conversion(fc, sc, amount):
    if fc == "£" and sc == "$":
        conversion = amount * 1.601
        return conversion
    elif fc == "£" and sc == "€":
        conversion = amount * 1.229
        return conversion
    elif fc == "$" and sc == "£":
        conversion = amount / 1.601
        return conversion
    elif fc == "$" and sc == "€":
        conversion = amount / 1.302
        return conversion
    elif fc == "€" and sc == "£":
        conversion = amount / 1.229
        return conversion
    elif fc == "€" and sc == "$":
        conversion = amount * 1.302
        return conversion

def give_results (conversion):
    print("{0} {1}".format(sc, conversion))

fc, sc, amount = get_currencies()
conversion = conversion (fc, sc, amount)
give_results(conversion)
