import math


def calculate_time_remaining(time, max_time=8 * 60):
    time = math.floor(time)
    remaining = max_time - time
    seconds = math.floor(remaining % 60)
    mins = math.floor((remaining - seconds) / 60)
    mins = str(mins)
    seconds = str(seconds)
    for i in range(2 - len(seconds)):
        seconds = "0" + seconds;

    for i in range(2 - len(mins)):
        mins = "0" + mins
    return mins + ":" + seconds
