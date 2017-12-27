import json
numbers = [2,334,34,5,56,56,32]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)