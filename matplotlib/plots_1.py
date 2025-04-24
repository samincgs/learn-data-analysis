from matplotlib import pyplot as plt

# add a default style to the gui
plt.style.use('fivethirtyeight')

# DATA

# x-axis values (age ranges)
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# y-axis values (median salaries)
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# python developers by age (no need since its repetitive)
# py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] 

# median python developer salaries (USD)
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# median javaScript developer salaries by age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

# plot the values (x, y) 
# change formatting of the plot
# can use format strings in the plot declaration if you want fmt = '[marker][line][color]'
# use plt.bar() for a bar chart instead
plt.plot(ages_x, py_dev_y, color='#5a7d9a', label='Python', linewidth=3) # # or use format string 'b'
plt.plot(ages_x, js_dev_y, color='#3b9d44', label='Javascript', linewidth=3)
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs') # or use format string '--k'

# give plot a title
plt.title('Median Salary (USD) by Age')

# give title for each axes
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)') 

# add a legend to identify plots
# plt.legend(['All Devs', 'Python']) # one way
plt.legend() # no need for arguments since label is there

# add a grid to the plot
# plt.grid(True)

# add plot parameters to add padding
plt.tight_layout()

# save as a png file
# plt.savefig('plots_1.png')

# show the plot when script is run
plt.show()