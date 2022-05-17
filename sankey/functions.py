from collections import OrderedDict

# # for testing
# #value= 'Gehalt [100] Budget \nDividenden [20] Budget \n\nBudget [70] Miete \nBudget [30] Konsum \nBudget [20] Sparen'


def link_colour(text):
    '''This function sets link colours'''
    colours = []

    text = text.split()
    text_chunks = list(chunks(text, 3)) # list of lists

    for i in text_chunks:
        colours.append('rgba(0,0,96,0.2)') 
    
    return colours


##################################################

def chunks(lst, n):
    """This funciotn yields successive n-sized chunks from a list."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


##################################################

def nodes(text):
    '''
    This function collects input from dcc.Textarea with user input and transforms it into 
    respective nodes and link.
    '''
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
        source_links.append(nodes.index(i))
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