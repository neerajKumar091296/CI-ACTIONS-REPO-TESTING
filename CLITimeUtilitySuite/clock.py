import time
from datetime import datetime

def digital_clock():
        print("Press Control + C to exit the loop")
        try:
            while True:
                current_time = datetime.now()
                custom_format = current_time.strftime("%B %d, %Y %H:%M")
                print(f"\rTime: {custom_format}",end ="",flush=True)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n Returning to Menu..")
            raise




def countdown_timer(seconds):

    if seconds <=0:
        print("Seconds must be greater than zero.")
        return
    print("Count Down Timer... Starts !")
    try:
        while seconds > 0:
            print(f"\rTime Remaining : {seconds}",end="",flush=True)
            time.sleep(1)
            seconds -= 1
    except KeyboardInterrupt:
        print("\n Countdown interrupted. Returning to Menu")
        pass




def run_pomodoro(work,short,long):
    total_work_seconds = work * 60
    total_short_seconds = short * 60
    total_longbreak_seconds = long * 60
    sessions = 0
    try:
        while True:
            print(" Focus Time")
            countdown_timer(total_work_seconds)
            sessions += 1

            if sessions %4  == 0:
                print("\n Long Break")
                countdown_timer(total_longbreak_seconds)
            else:
                print("\n Short Break")
                countdown_timer(total_short_seconds)
    except KeyboardInterrupt:
        print("\n Pomodoro Timer Interrupted. Returning to Menu")



