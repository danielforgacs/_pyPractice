def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


a = {
    '1': 'None',
    '2': '22',
    '3': ['33'],
    '4': ['33', '44', '55'],
    # 4: {},
    '5': {'5': '55'},
    '6': {'66': {'667': '668'}},
    '6b': {'66': {'667': '668', '667b': '668B', '667cc': '667cc'}},
    '7': {'77': {'777': {'7777': {'7878': ('7777',)}}}}
}

from pprint import pprint

# print flatten_json(a)
pprint(flatten_json(a))