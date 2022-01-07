import pyautogui as pg
from time import sleep

def keyboard():
    value = input("value > ")
    loop = int(input("for > "))
    wait = int(input("sleep > "))
    input("ready ? ")
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    sleep(1)
    print("START")
    sleep(1)
    arr = []
    arr.append(value)
    arr.append(loop)
    arr.append(wait)
    return arr

while 1:
    res = input("1 - press \n2 - write \n\n/> ")
    
    if res == "1":
        arr = keyboard()
        for i in range(arr[1]):
            print(arr[1] - i - 1, "left")
            pg.press(arr[0])
            sleep(arr[2])
        print("END \n")

    elif res == "2":
        interval = input("interval > ")
        arr = keyboard() 
        for i in range(arr[1]):
            print(arr[1] - i - 1, "left")
            pg.write(arr[0], interval = float(interval))
            sleep(arr[2])
        print("END \n")