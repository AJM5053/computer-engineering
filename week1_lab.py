# A basic print
print("Hello world")
# A print using variables
student_name = "Adam"
student_age = "22"
print("Student name:", student_name)
print("Student age:", student_age)
# Addition using variables
num1 = 7689
num2 = 5683
total = num1 + num2
print("The total is", total)
# User profile inside a box
boxed_name = "Jack"
boxed_username = "JackP02"
boxed_location = "Bristol"
box_width = 40
border = "+" + "-" * (box_width - 2) + "+"
line_name = f"| Name: {boxed_name:<{box_width - 9}}|"
line_username = f"| Username: {boxed_username:<{box_width - 13}}|"
line_location = f"| Location: {boxed_location:<{box_width - 13}}|"
print(border)
print(line_name)
print(line_username)
print(line_location)
print(border)
# A list of F1 teams in a box
mclaren = "McLaren"
mercedes = "Mercedes"
ferrari = "Ferrari"
red_bull_racing = "Red Bull Racing"
williams = "Williams"
racing_bulls = "Racing Bulls"
aston_martin = "Aston Martin"
kick_sauber = "Kick Sauber"
haas = "Hass"
alpine = "Alpine"
box_width2 = 30
border2 = "+" + "-" * (box_width2 - 2) + "+"
line_mclaren = f"| {mclaren:<{box_width2 - 3}}|"
line_mercedes = f"| {mercedes:<{box_width2 - 3}}|"
line_ferrari = f"| {ferrari:<{box_width2 - 3}}|"
line_red_bull_racing = f"| {red_bull_racing:<{box_width2 - 3}}|"
line_williams = f"| {williams:<{box_width2 - 3}}|"
line_racing_bulls = f"| {racing_bulls:<{box_width2 - 3}}|"
line_aston_martin = f"| {aston_martin:<{box_width2 - 3}}|"
line_kick_sauber = f"| {kick_sauber:<{box_width2 - 3}}|"
line_haas = f"| {haas:<{box_width2 - 3}}|"
line_alpine = f"| {alpine:<{box_width2 - 3}}|"
print(border2)
print(line_mclaren)
print(line_mercedes)
print(line_ferrari)
print(line_red_bull_racing)
print(line_williams)
print(line_racing_bulls)
print(line_aston_martin)
print(line_kick_sauber)
print(line_haas)
print(line_alpine)
print(border2)