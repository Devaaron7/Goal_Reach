import os

title = input("Enter A Title\n")

goal = input("Enter A Goal\n")

week = input("Enter A Week\n")

s_goal = input("Enter A Sub Goal\n")

paste = """

<!DOCTYPE html>
<html>
<body>

<h1>{}</h1>
<h3>{}</h3>
<h4>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp{}:</h4>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<label><input type="checkbox" name="myCheckbox"> {g}</label>
<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<label><input type="checkbox" name="myCheckbox"> {g}</label>
<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<label><input type="checkbox" name="myCheckbox"> {g}</label>
<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<label><input type="checkbox" name="myCheckbox"> {g}</label>

</body>
</html>





""".format(title, s_goal, week, g = goal)


f = open("test.html", "w")
f.write(paste)
f.close()


