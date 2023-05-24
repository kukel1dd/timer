from time import sleep

def timer(min, sec):
    sleep(1)
    if min < 0:
        print("Invalid Time.")
        return False
    if sec > 60:
        converted_min = sec // 60 
        min += converted_min 
        sec = sec % 60 
    elif  sec < 0:
        print("invalid time.")
        return False

    while True:
        sleep(1)
        if sec < 10:
            print(f"{min}:0{sec}")
        else:
            print(f"{min}:{sec}")
        sec -= 1
        if sec <= -1:
            sec += 60
            min -= 1    
        if min < 0:
            print("Times up!")
            return False

timer(0, 1000)
    