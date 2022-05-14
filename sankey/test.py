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

# indices = range(len(ls_value)) 
# labels = [ls_value[i] for i in indices if not ls_value[i].startswith('[')] # all labels (with duplicates)

# unique_labels = list(sorted(set(ls_value), key=ls_value.index)) # unique labels
# indices_unique = range(len(unique_labels))
# unique_labels = [unique_labels[i] for i in indices_unique if not unique_labels[i].startswith('[')]

# print(labels)
# print(unique_labels)
# print(ls_value)

def node_label(text):

    '''
    This function evaluates a string of user input and filters for node label in correct order.
    The function goes through the list of words.
    At each step: 
      - evaluate if the word has been there already, if not, put them in a list called 'past'
      - index for while loop increases by three for unseen worde
      - if word was already there, subtract index by one, then continue by adding 3
    '''
    ls_value = text.split()
    past = []
    i = 0
    while i < len(ls_value):
        if ls_value[i] not in past and not ls_value[i].startswith('['):
            past.append(ls_value[i])
            i = i + 3
        if i < len(ls_value) and ls_value[i] in past:
            i = i - 1
            past.append(ls_value[i])
            i = i + 3
    return past

#print(node_label(value))


#print("END")
