import os


paste1 = """

<style>

table.blueTable {
border: 1px solid #05131C;
width: 100%;
text-align: left;
border-collapse: collapse;
}
table.blueTable td, table.blueTable th {
border: 1px solid #AAAAAA;
padding: 3px 2px;
}
table.blueTable tbody td {
font-size: 13px;
}
table.blueTable thead {
background: #000000;
background: -moz-linear-gradient(top, #404040 0%, #191919 66%, #000000 100%);
background: -webkit-linear-gradient(top, #404040 0%, #191919 66%, #000000 100%);
background: linear-gradient(to bottom, #404040 0%, #191919 66%, #000000 100%);
border-bottom: 2px solid #444444;
}
table.blueTable thead th {
font-size: 15px;
font-weight: bold;
color: #FFFFFF;
border-left: 2px solid #D0E4F5;
}
table.blueTable thead th:first-child {
border-left: none;
}

table.blueTable tfoot td {
font-size: 14px;
}


</style>
"""

Total_Paste = ""

Total_Paste += paste1

running = True

while running:

    goal = input("Enter A Goal\n")

    s_goal = input("Enter A Sub Goal\n")

    paste2 = """



    <h2> {g} </h2>

    <table class="blueTable">
    <thead>
    <tr>
    <th>Week 1</th>
    <th>Week 2</th>
    <th>Week 3</th>
    <th>Week 4</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>{sg} 1 item 1</td>
    <td>{sg} 2 item 1</td>
    <td>{sg} 3 item 1</td>
    <td>{sg} 4 item 1</td>
    </tr>
    <tr>
    <td>{sg} 1 item 2</td>
    <td>{sg} 2 item 2</td>
    <td>{sg} 3 item 2</td>
    <td>{sg} 4 item 2</td>
    </tr>
    <tr>
    <td>{sg} 1 item 3</td>
    <td>{sg} 2 item 3</td>
    <td>{sg} 3 item 3</td>
    <td>{sg} 4 item 3</td>
    </tr>
    <tr>
    <td>{sg} 1 item 4</td>
    <td>{sg} 2 item 4</td>
    <td>{sg} 3 item 4</td>
    <td>{sg} 4 item 4</td>
    </tr>
    </tbody>
    </table>

    <br>



    """.format(sg = s_goal, g = goal)

    Total_Paste += paste2

    choice = input("Do you want to enter another goal? Please enter y or n\n")
    if choice == "y":
        pass
    if choice == "n":
        running = False




f = open("test.html", "w")
f.write(Total_Paste)
f.close()


