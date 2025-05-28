import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

# language_count = {}

# 1. way to open csv with csv module
# dev_data_file = open('matplotlib/2_dev_data.csv')

# data_csv = csv.DictReader(dev_data_file)

data_csv = pd.read_csv('matplotlib/2_dev_data.csv')
user_ids = data_csv['Responder_id']
user_languages = data_csv['LanguagesWorkedWith']


# print(data_csv)
# 2. open csv with pandas

counter = Counter()

# start_time = time.time()

# option 1 (manual dictionary)
# for row in data_csv:

#     user_languages = row['LanguagesWorkedWith'].split(';')
    
#     # for language in user_languages:
#     #     if language not in language_count:
#     #         language_count[language] = 1
#     #     else:
#     #         language_count[language] += 1
    
#     # use the counter built in Counter from collections (comes sorted)
#     counter.update(user_languages)
            
# print(language_count)

# option 2 with pd data
for lang in user_languages:
    counter.update(lang.split(';'))

languages = []
popularity = []

# print(counter)

# print(counter.most_common(5)) # can get the top 5 using this method
# seperate tuples into x and y axis values
for lang, count in counter.most_common(15):
    languages.append(lang)
    popularity.append(count)
    
# dev_data_file.close()

print(languages)
print(popularity)

languages.reverse()
popularity.reverse()

plt.title('Most Popular Languages')
# plt.ylabel('Programming Languages') # redundant
plt.xlabel('Count of Users')
plt.barh(languages, popularity) # horizontal bar chart

# end_time = time.time() - start_time

plt.tight_layout()

# print(f'It took {end_time}') # 0.3s
plt.show()