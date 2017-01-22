from pprint import pprint

db = {
    '1': {'2': {'3': '4'}},
    '2': {'22': {'33': '44'}},
}

newdict = {}

if isinstance({'1': {'2': {'3': '4'}}}, dict):
        key = '1'

        if isinstance({'2': {'3': '4'}}, dict):
            key = '1_2'

            if isinstance({'3': '4'}, dict):
                key = '1_2_3'

                if isinstance('4', dict):
                    pass
                else:
                    newdict = {'1_2_3': '4'}


def flatter(dict_, basekey='', newdict={}):
    for key, value in dict_.items():
        if not basekey:
            flat_key = key
        else:
            flat_key = basekey + '_' + key

        flat_value = value
        # print('\t', key)
        # print('\t', value)
        # print('\t', flat_key)

        if isinstance(value, dict):
            flatter(value, flat_key)
        else:
            newdict[flat_key] = flat_value
            return newdict

    return newdict



result = flatter(db)
pprint(result)
print(result.keys())
print(result.values())