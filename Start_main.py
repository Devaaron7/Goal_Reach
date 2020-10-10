import time

goals = {}

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

def add_goal():
    goal = input("Type the goal you would like to work on this month - ex. Complete a new book, or Head to the Gym twice a week. \n")
    time.sleep(2)
    time = int(input("Type the the hours needed to complete this goal - ex. A 300 page book will take me 30 hours to complete, or I spend 1.5 hours at the Gym, so 3 hours a week if I go twice. \n"))
    time.sleep(2)
    goals[goal] = time
    time.sleep(2)
    print("Goal added to log")

intro()

print("Great, ok - lets start assigning some goals to complete") 

print(goals)

add_goal()

print(goals)

add_goal()

print(goals)


