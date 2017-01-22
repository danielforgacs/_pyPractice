from pprint import pprint

db = {
    '1': {'2': {'3': '4'}},
    '2': {'22': {'33': '44'}},
    '3': [333, 444, 555],
    4: 4,
    5: {55: {555: 55555}}
}

# if isinstance({'1': {'2': {'3': '4'}}}, dict):
#         key = '1'
#         if isinstance({'2': {'3': '4'}}, dict):
#             key = '1_2'
#             if isinstance({'3': '4'}, dict):
#                 key = '1_2_3'
#                 if isinstance('4', dict):
#                     pass
#                 else:
#                     newdict = {'1_2_3': '4'}

def flatter(dict_, basekey='', newdict={}):
    for key, value in dict_.items():
        if not basekey:
            flat_key = key
        else:
            flat_key = str(basekey) + '_' + str(key)

        flat_value = value

        if isinstance(value, dict):
            flatter(value, flat_key)
        else:
            newdict[flat_key] = flat_value

    return newdict



result = flatter(db)
print(list(result.keys()))
print(list(result.values()))
print()
pprint(result)