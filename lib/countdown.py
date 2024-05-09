import time
def countdown(int):
    while True:
        print(f"{int} SECOND(S)!")
        int -= 1
        if int == 0:
            print("HAPPY NEW YEAR!")
            break

countdown(5)


def countdown_with_sleep(seconds):
    while True:
        print(seconds)
        seconds -= 1
        if seconds < 0:
            print(f"{seconds} SECOND(S)!")
        if seconds == 0:
            print("HAPPY NEW YEAR!")
            time.sleep(1)
            break


countdown_with_sleep(5)