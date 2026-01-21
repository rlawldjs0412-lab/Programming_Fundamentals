'''
codewars.Swap_items_in_a_dictionary의 Docstring

In this kata, you will take the keys and values of a dict and swap them around.

You will be given a dictionary, and then you will want to return a dictionary with the old values as the keys, and list the old keys as values under their original keys.

For example, given the dictionary: {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'},

you should return: {'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}

Notes:

The dictionary given will only contain strings
The dictionary given will not be empty
You do not have to sort the items in the lists
'''

def switch_dict(d):
    result = {}

    for key, value in d.items():
        if value not in result:
            result[value] = []
            
        result[value].append(key)

    return result
