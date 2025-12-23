
from inputs import *
import time
from clock import *


while True:
        show_menu()
        user_input = get_user_choice()

        if user_input == 1:
            try:
                digital_clock()
            except KeyboardInterrupt:
                pass
        elif user_input == 2:
            try:
                seconds = int(input("Enter input in seconds"))
                countdown_timer(seconds)
            except ValueError:
                print("Please enter a valid number.")

        elif user_input == 3:
            try:
                work,short,long = user_prompt()
                run_pomodoro(work, short, long)
            except KeyboardInterrupt:
                pass
        elif user_input == 4:
            print("Good Bye")
            break

        else:
            print("Invalid choice")



