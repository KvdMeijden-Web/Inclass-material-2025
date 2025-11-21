# import time
# import os

# seconds = 0
# def set_timer():
#     timer = int(input("how many seconds?"))
#     return timer

# def clock():
#     minutes = seconds//60
#     hours = minutes//60

#     minutes_left = minutes%60
#     seconds_left = seconds%60

#     if seconds_left < 10:
#         seconds_left = f"0{seconds_left}"
#     if minutes_left <60:
#         minutes_left = f"0{minutes_left}"
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(f"{hours}:{minutes_left}:{seconds_left}")

# set_timer = set_timer()
# while True:
#     time.sleep(1)
#     seconds += 1
#     clock()
#     if set_timer == seconds:
#         print("Alarm")
#         break

import time
# % it shows the remainder of a division
# // it shows rounds the division down

counter = 0

def timer(counter):
    time.sleep(1)
    counter = counter+ 1
    return counter

def clock(count):
    minutes = count // 60
    seconds_left = count % 60
    print(f"{minutes}:{seconds_left}")

def main():
    alarm_time = int(input("What time do you set the alarm in seconds"))
    while True:
        counter = timer(counter)
        clock(counter)

main()
