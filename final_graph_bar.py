
import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

def coordinate():
    x_row = ('Algebra 2', 'AP Computer Science', 'History', 'English 1', 'Biology')
    my_y_row_input = input("5 items please:")
    if len(my_y_row_input) <= 1:
        print('you have not read the prompt correctly!')
        coordinate()
    else:
        my_y_row = tuple(map(str, my_y_row_input.split(" ")))
        print(my_y_row, type(my_y_row))
        if len(my_y_row) != len(x_row):
            print(f"you put {len(my_y_row)}, but need {len(x_row)}")
            coordinate()
        else:
            y_row = my_y_row
            fig = plt.figure()
            plt.yticks(np.arange(0, len(my_y_row)))
            plt.bar(x_row, y_row)
            fig.set_size_inches(10, 4.8)
            plt.show()
            print(my_y_row, type(my_y_row))
            pass