import time, os, random

goals = {}
key = []

def sel_month():
    months = ["Null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    print("""
    1. January
    2. February
    3. March
    4. April
    5. May
    6. June
    7. July
    8. August
    9. September
    10. October
    11. November
    12. December
    """)


    choice = int(input("Type a number to select the month you need\n"))
    while choice <= 0 or choice >= 13:
        choice = int(input("Invalid Choice. Please chose again\n"))
    
    gmonth = months[choice]
    return gmonth

gmonth = ""

def clear():
    os.system( "cls" )

def intro():
    global gmonth
    clear()
    print("Welcome to A New Month - Lets set some goals")
    time.sleep(2)
    clear()
    gmonth += sel_month()
    #print("Current Unallocated time: ", w_time)
    work_time = int(input("How many hour per week do you want to use for your Goals? \n"))
    w_time = 0
    w_time += work_time
    clear()
    print("""Ok, so weekly, You have""", w_time,""" hours available to work on your goals.""")
    m_time = w_time * 4
    time.sleep(2)
    clear()
    print("Thats", m_time, " hours for the month.") 
    time.sleep(3)
    return m_time

def add_goal():
    global time_balance
    running = True
    while running:
        clear()
        print("Remaining Time for the Month: ", time_balance)
        print("Current Goal List for {}: ".format(gmonth), goals)
        goal = input("""Type the goal you would like to work on this month - ex. Complete a new book, or Head to the Gym twice a week. \n""")
        key.append(goal)
        time.sleep(2)
        print("\nType the hours needed to complete this goal.")
        print("Ex. If a 300 page book will take you 30 hours to complete, enter 30")
        duration = int(input("Or if you want to workout twice a week, and each session is 1 hour. Enter 8 for a four week month.\n"))
        time.sleep(2)
        goals[goal] = duration
        clear()
        time.sleep(2)
        print("Goal added to log")
        time_balance -= duration
        print("Remaining amount of time for month: ", time_balance)
        time.sleep(2)
        clear()
        if time_balance <= 2:
            print("We're running out of available time for more goals --- current balance is: ", time_balance)
            #running = False
            break
        print("Do you want to add another goal for the month? Type 'y' for yes or 'n' for no \n")
        choice = input()
        if choice == "y":
            clear()
            pass
        if choice == "n":
            running = False

def ending():
    global goals
    global key
    clear()
    print("Ok, lets think ahead...")
    time.sleep(2)
    print("It's the end of the month, and here is all the goals you have completed:")
    time.sleep(2)
    for x in goals:
        print(x)
    time.sleep(2)
    print("Exporting a checklist for you to print out - Lets start tracking your goals!")
    time.sleep(1)
    
time_balance = intro() 

clear()

print("Ok - lets start assigning some goals to complete") 

add_goal()

ending()

