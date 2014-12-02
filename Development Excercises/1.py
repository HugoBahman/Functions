#Hugo
#Development Excercise 1

def get_time():
    hours = int(input("How many hours: "))
    minutes = int(input("How many mintues: "))
    seconds = int(input("How many seconds: "))
    return hours, minutes, seconds

def calculate_seconds(hours, minutes, seconds):
    hour_seconds = hours*60*60
    minute_seconds = minutes*60
    total_seconds = hour_seconds + minute_seconds + seconds
    return total_seconds

def display_result(total_seconds):
     print("{0} seconds".format(total_seconds))

hours, minutes, seconds = get_time()
total_seconds = calculate_seconds(hours, minutes, seconds)
display_result(total_seconds)
