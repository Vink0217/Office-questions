'''
Q8) List Flattening 
Flatten a nested list, e.g., [1, [2, 3], [4, [5, 6]]] → [1, 2, 3, 4, 5, 6]. 
'''
def flatten(list_given):
    flattened_list = []
    for i in list_given:
        if isinstance(i, list):
            flattened_list.extend(flatten(i))
        else:
            flattened_list.append(i)
    return flattened_list

given_list = [1, [2, 3], [4, [5, 6]]]
flat_list = flatten(given_list)
print(flat_list)
