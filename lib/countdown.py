import time
def countdown(int):
    while True:
        print(int)
        int -= 1
        if int == 0:
            print("HAPPY NEW YEAR!")
            break


def countdown_with_sleep(int):
    while True:
        print(int)
        int -= 1
        if int == 0:
            print("HAPPY NEW YEAR!")
            break
        time.sleep(1)

countdown_with_sleep(10)