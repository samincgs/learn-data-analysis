import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')

labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

labels = labels[:5]
slices = slices[:5]

explode = [0, 0, 0, 0.1 ,0] # adds padding to seperate from the radius of the circle and show emphasis

plt.title('Pie Charts')


# autopct is important, it shows the percentage of each slice formatted
plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'}, explode=explode, autopct='%1.1f%%') # can add shadow with shadow=True, can change startangle with a number startangle=90

plt.tight_layout()

plt.show()