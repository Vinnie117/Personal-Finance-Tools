from enum import unique
import re
import yaml

with open('A:\Projects\Personal-Finance-Tools\sankey\complex_sankey_data.yaml', 'r') as file:
    data = yaml.safe_load(file)

ls = data['data'][0]['node']['label']
#print(ls)

############

value= 'Gehalt [100] Budget \nDividenden [20] Budget \n\nBudget [70] Miete \nBudget [30] Konsum \nBudget [20] Sparen'
print(value)  # -> ['Gehalt', 'Dividenden', 'Budget', 'Miete', 'Konsum', 'Sparen'] extrahieren!
ls_value = value.split()
print(ls_value)

print(ls_value[0,1])

unique_values = list(set(value.split()))
x = re.findall('([A-Z])\w+', str(unique_values))

print(x)










