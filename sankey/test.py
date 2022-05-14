from enum import unique
import re
import yaml
from itertools import tee, islice, chain

with open('A:\Projects\Personal-Finance-Tools\sankey\complex_sankey_data.yaml', 'r') as file:
    data = yaml.safe_load(file)

ls = data['data'][0]['node']['label']
#print(ls)

############

value= 'Gehalt [100] Budget \nDividenden [20] Budget \n\nBudget [70] Miete \nBudget [30] Konsum \nBudget [20] Sparen'
#print(value)  # -> ['Gehalt', 'Dividenden', 'Budget', 'Miete', 'Konsum', 'Sparen'] extrahieren!

ls_value = value.split() # split string into a list

indices = range(len(ls_value)) 
labels = [ls_value[i] for i in indices if not ls_value[i].startswith('[')] # all labels (with duplicates)

unique_labels = list(sorted(set(ls_value), key=ls_value.index)) # unique labels
indices_unique = range(len(unique_labels))
unique_labels = [unique_labels[i] for i in indices_unique if not unique_labels[i].startswith('[')]

print(labels)
print(unique_labels)
print(ls_value)

# Order we want: [Gehalt, Dividenden, Budget, Miete, Konsum, Sparen]
index = [0,3,6,9]
past = []

# for i in ls_value[::3]:
#     if i not in past and not i.startswith('['):
#         past.append(i)
#         print(i)
#     if i in past:
#         i-1 

# print(past)

i = 0
while i < len(ls_value)-1:
    if ls_value[i] not in past and not ls_value[i].startswith('['):
        past.append(ls_value[i])
        i = i + 3
    if ls_value[i] in past:
        i = i - 1
        past.append(ls_value[i])
        print(ls_value[i])
        i = i + 3

print(past)


print("END")
