from enum import unique
import re
import yaml
from itertools import tee, islice, chain
import numpy as np
from collections import OrderedDict


with open('A:\Projects\Personal-Finance-Tools\sankey\complex_sankey_data.yaml', 'r') as file:
    data = yaml.safe_load(file)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

ls = data['data'][0]['node']['label']

value= 'Gehalt [100] Budget \nDividenden [20] Budget \n\nBudget [70] Miete \nBudget [30] Konsum \nBudget [20] Sparen'
test = value.split() # split string into a list
#print(test)
############


def nodes(text):

    text = text.split()
    text_chunks = list(chunks(text, 3))

    source_nodes = []
    target_nodes = []

    # extracting unique node labels
    for i in text_chunks:
        source_nodes.append(i[0])
        target_nodes.append(i[2])
    nodes = list(OrderedDict.fromkeys(source_nodes+target_nodes))

    # determining link flows
    source_links=[]
    target_links=[]
    for i in source_nodes:
        source_links.append(source_nodes.index(i))
    for i in target_nodes:
        target_links.append(nodes.index(i))

    return nodes, source_links, target_links



##################################################

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


##################################################################################

# value_chunks = list(chunks(test, 3))
# print(value_chunks)

# source_nodes = []
# target_nodes = []

# for i in value_chunks:
#     source_nodes.append(i[0])
#     target_nodes.append(i[2])

# print('Source nodes: ', source_nodes)
# print('Target nodes: ', target_nodes)

# nodes = list(OrderedDict.fromkeys(source_nodes+target_nodes))
# print(nodes)

# source_links=[]
# target_links=[]

# for i in source_nodes:
#     source_links.append(source_nodes.index(i))

# for i in target_nodes:
#     target_links.append(nodes_nodes.index(i))


# print(source_links)
# print(target_links)


############

# resulting_list = list(source_nodes)
# # Combining two lists and removing duplicates, without removing duplicates in original list
# resulting_list.extend(x for x in target_nodes if x not in resulting_list)
# #print(resulting_list)
# # Get unique values
# indexes = np.unique(resulting_list, return_index=True)[1] # array of indices
# #print(indexes)
# see = [resulting_list[index] for index in sorted(indexes)]
# #print(see)

############

# def node_label(text):

#     '''
#     This function evaluates a string of user input and filters for node label in correct order.
#     The function goes through the list of words.
#     At each step: 
#       - evaluate if the word has been there already, if not, put them in a list called 'past'
#       - index for while loop increases by three for unseen worde
#       - if word was already there, subtract index by one, then continue by adding 3
#     '''
#     ls_value = text.split()
#     past = []
#     i = 0
#     while i < len(ls_value):
#         if ls_value[i] not in past and not ls_value[i].startswith('['):
#             print(ls_value[i])
#             past.append(ls_value[i])
#             print(past)
#             i = i + 3
#             print(i)
#         if i <= len(ls_value) and ls_value[i] in past:
#             i = i - 1
#             past.append(ls_value[i])
#             i = i + 3
#     return past

# print(node_label(value))

