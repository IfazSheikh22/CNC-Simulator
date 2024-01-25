# Define a class to represent a G-code command
class Command:
    def __init__(self, type, x, y):
        self.type = type  # The type of the command (e.g., 'G00', 'G01')
        self.x = x  # The X-coordinate for the command
        self.y = y  # The Y-coordinate for the command

# Function to parse G-code from a string into Command objects
def parse_gcode(gcode):
    lines = gcode.split('\n')  # Split the G-code into lines
    commands = []  # List to hold the parsed commands
    for line in lines:  # For each line of G-code...
        parts = line.split(' ')  # Split the line into parts
        type = parts[0]  # The first part is the command type
        x = float(parts[1][1:])  # The second part is the X-coordinate (remove 'X' and convert to float)
        y = float(parts[2][1:])  # The third part is the Y-coordinate (remove 'Y' and convert to float)
        commands.append(Command(type, x, y))  # Create a Command object and add it to the list
    return commands  # Return the list of commands

# Function to simulate the tool path from a list of commands
def simulate_tool_path(commands):
    path = []  # List to hold the points in the tool path
    for command in commands:  # For each command...
        if command.type == 'G00' or command.type == 'G01':  # If the command is 'G00' or 'G01'...
            path.append((command.x, command.y))  # Add the point to the tool path
    return path  # Return the tool path

# Function to display the tool path
def display_tool_path(path):
    for point in path:  # For each point in the path...
        print(f'X{point[0]} Y{point[1]}')  # Print the point

# Test the simulator with some G-code
gcode = """
G00 X0 Y0
G01 X10 Y10
G00 X20 Y20
G01 X30 Y30
"""

commands = parse_gcode(gcode)  # Parse the G-code into commands
path = simulate_tool_path(commands)  # Simulate the tool path from the commands
display_tool_path(path)  # Display the tool path
