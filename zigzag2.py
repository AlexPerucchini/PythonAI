import time, sys
indent = 0  # How many spaces to indent
rows = 0 # How many rows to create
indent_increasing = True  # Whether the indentation is increasing or not

try:
    while rows < 10:  # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second.

        if indent_increasing:
             # Increase the number of spaces:
             indent = indent + 1
             if indent == 5:
                 # Change direction:
                 indent_increasing = False
        else:
             # Decrease the number of spaces:
             indent = indent - 1
             if indent == 0:
                 # Change direction:
                 indent_increasing = True

        rows = rows + 1
except KeyboardInterrupt:
    sys.exit()
