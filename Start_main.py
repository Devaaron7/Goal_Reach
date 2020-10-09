import time

def intro():
    print("Welcome to A New Month - Lets set some goals")
    time.sleep(2)
    w_time = 168
    print("Everyone has the same amount of time")
    time.sleep(2)
    print("It's how we spend it that makes us different")
    time.sleep(2)
    print("Current Unallocated time: ", w_time)
    work_time = int(input("Enter how many hours a week you spend working \n"))
    w_time -= work_time
    time.sleep(2)
    print("Current Unallocated time: ", w_time)
    time.sleep(2)
    sleep_time = int(input("Enter how many hours of sleep you get a night \n")) * 7
    w_time -= sleep_time
    time.sleep(2)
    print("Current Unallocated time: ", w_time)
    time.sleep(2)
    human_time = w_time / 3
    w_time -= round(human_time, -1)
    print("""While it's great to try and be perfect, shit happens. We'll deduct a fraction of 
    available time and chalk it up to being human.""")
    time.sleep(2)
    print("Current Unallocated time: ", w_time)
    time.sleep(2)
    print("""Ok, so weekly, after deducting Work, Sleep, and some padding 
    - You have""", w_time,""" hours left to work on your goals.""")
    m_time = w_time * 4
    time.sleep(2)
    print("Thats", m_time, " hours for the month.") 
    time.sleep(2)
    return w_time

intro()

print("Great, ok - lets start assigning some goals to complete") 