from pickletools import long1


def show_menu():
    print("""
        ==========================
        ⏱  Time Utility Suite
        ==========================
        1. Digital Clock
        2. Countdown Timer
        3. Pomodoro Timer
        4. Exit
        ==========================
    """)



def get_user_choice() -> int:
    choice = int(input("Enter your choice: "))
    return choice



def get_duration(prompt: str,default: int, min_value: int) -> int:
    while True:
        user_input = input(f"{prompt} (default {default}): ").strip()

        if user_input == "":
            return default

        if not user_input.isdigit():
            print("Please enter a valid number. ")
            continue
        value = int(user_input)
        if value < min_value:
            print(f"Value must be at least {min_value} minutes. ")
            continue

        return  value



def user_prompt() -> tuple[int,int,int]:
    work = get_duration("Work duration in minutes",25,1)
    short = get_duration("Short break duration in minutes",5,1)
    long = get_duration("Long break duration in minutes",15,5)
    return  work,short,long
