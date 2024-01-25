**CNC Simulator**

**Objective:** To create a CNC simulator that can interpret a subset of G-code commands and display the resulting tool path on the screen.

**Steps:**

1. **Define G-code Commands:** Define a small set of G-code commands that your simulator will support. For simplicity, could start with just two commands: `G00` (rapid positioning) and `G01` (linear interpolation).

2. **Parse G-code:** Write a function that can parse these commands from a string of G-code. This function should return a list of commands, where each command is represented as a dictionary with keys for the command type and parameters.

3. **Simulate Tool Path:** Write a function that takes a list of commands and simulates the tool path. This function should return a list of points representing the path of the tool.

4. **Display Tool Path:** Write a function that takes a list of points and displays the tool path on the screen. Could use a simple graphics library for this, or even just print the points to the console.

5. **Test Simulator:** Once everything is set up, test the CNC simulator by feeding it some G-code and checking that it correctly displays the tool path.
