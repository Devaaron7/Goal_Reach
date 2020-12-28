import os

'''
Logic to display correct Hours / Minutes for Divided Goal Time

# Divide into 4 with hours and minutes

## 10 - 2 Hours & 30 Minutes outputted

i = 7.5 # Hours

m = i * 60  # minutes

d = m / 4

re_hr = d // 60

re_min = d % 60

if re_min == 0:
    print("If divided by 4, it was take you {} hour(s) to complete".format(int(re_hr)))
elif re_hr == 0:
    print("If divided by 4, it was take you {} minutes to complete".format(int(re_min)))
else:
    print("If divided by 4, it was take you {} hours & {} minutes to complete".format(int(re_hr), int(re_min)))

'''


t = {"Test 1": 10, "Test 2": 16, "Test 3": 25}

paste_start = """

<!DOCTYPE html>
<html>
<body>

<style>

.control {
font-family: arial;
display: block;
position: relative;
padding-left: 36px;
margin-bottom: 15px;
padding-top: 3px;
cursor: pointer;
font-size: 17px;
}
.control input {
position: absolute;
z-index: -1;
opacity: 0;
}
.control_indicator {
position: absolute;
top: 2px;
left: 0;
height: 20px;
width: 20px;
background: #e6e6e6;
border: 1px solid #000000;
border-radius: 0px;
}
.control:hover input ~ .control_indicator,
.control input:focus ~ .control_indicator {
background: #cccccc;
}

.control input:checked ~ .control_indicator {
background: #2aa1c0;
}
.control:hover input:not([disabled]):checked ~ .control_indicator,
.control input:checked:focus ~ .control_indicator {
background: #0e6647d;
}
.control input:disabled ~ .control_indicator {
background: #e6e6e6;
opacity: 0.6;
pointer-events: none;
}
.control_indicator:after {
box-sizing: unset;
content: '';
position: absolute;
display: none;
}
.control input:checked ~ .control_indicator:after {
display: block;
}
.control-checkbox .control_indicator:after {
left: 8px;
top: 4px;
width: 3px;
height: 8px;
border: solid #ffffff;
border-width: 0 2px 2px 0;
transform: rotate(45deg);
}
.control-checkbox input:disabled ~ .control_indicator:after {
border-color: #7b7b7b;
}

{display: inline-block; *display: inline; zoom: 1; vertical-align: top; font-size: 12px;}


.weektitle {
width: 100%;
float: left;
padding: 5px;
border: 0px solid red;
}


.week1 {
width: 20%;
float: left;
padding: 5px;
border: 0px solid red;
}

.week2 {
width: 20%;
float: left;
padding: 5px;
border: 0px solid red;
}

.week3 {
width: 20%;
float: left;
padding: 5px;
border: 0px solid red;
}


.week4 {
width: 20%;
float: left;
padding: 5px;
border: 0px solid red;
}

</style>

"""

paste_end = """

</body>
</html>

"""

Total_Paste = ""

Total_Paste += paste_start

running = 0

running += len(t)

while running != 0:

    goal = input("Enter A Goal\n")

    s_goal = input("Enter A Sub Goal\n")

    paste2 = """

        <div class="weektitle">

        <h1> {g} </h1>

        </div>


        <div class="week1">

        <h2> Week 1 </h2>

        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" disabled="disabled" />
        <div class="control_indicator"></div>
        </div>


        <div class="week2">

        <h2> Week 2 </h2>

        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" disabled="disabled" />
        <div class="control_indicator"></div>

        </div>


        <div class="week3">

        <h2> Week 3 </h2>


        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" disabled="disabled" />
        <div class="control_indicator"></div>

        </div>


        <div class="week4">

        <h2> Week 4 </h2>


        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" />
        <div class="control_indicator"></div>
        </label>
        <label class="control control-checkbox">
        {sg}
        <input type="checkbox" disabled="disabled" />
        <div class="control_indicator"></div>

        </div>

    """.format(sg = s_goal, g = goal)

    Total_Paste += paste2

    choice = input("Do you want to enter another goal? Please enter y or n\n")
    if choice == "y":
        pass
    if choice == "n":
        running = False


Total_Paste += paste_end

f = open("test.html", "w")
f.write(Total_Paste)
f.close()


