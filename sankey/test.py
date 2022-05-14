from enum import unique
import re
import yaml
from itertools import tee, islice, chain

with open('A:\Projects\Personal-Finance-Tools\sankey\complex_sankey_data.yaml', 'r') as file:
    data = yaml.safe_load(file)

ls = data['data'][0]['node']['label']

value= 'Gehalt [100] Budget \nDividenden [20] Budget \n\nBudget [70] Miete \nBudget [30] Konsum \nBudget [20] Sparen'
test = value.split() # split string into a list
############

print(test)

source_nodes = []
target_nodes = []

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
            print(ls_value[i])
            past.append(ls_value[i])
            print(past)
            i = i + 3
            print(i)
        if i <= len(ls_value) and ls_value[i] in past:
            i = i - 1
            past.append(ls_value[i])
            i = i + 3
    return past

print(node_label(value))


def link_value(text):
    '''
    This function evaluates a string of user input and filters for the flow values, 
    i.e. thickness of links
    '''
    ls_value = text.split()
    flows = []
    i = 1

    while i < len(ls_value):
        flow = int(ls_value[i][1:-1])
        flows.append(flow)
        i = i + 3

    return flows


#print("END")
