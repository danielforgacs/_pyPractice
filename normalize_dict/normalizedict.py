from pprint import pprint

basedict = {
    '1': 'None',
    '2': '22',
    '3': ['33'],
    '4': ['33', '44', '55'],
    '5': {'5': '55'},
    '5b': {'5b': ['b55', 'b5555']},
    '6': {'66': {'667': '668'}},
    '6b': {'66': {'667': '668', '667b': '668B', '667cc': '667cc'}},
    '7': {'77': {'777': {'7777': {'7878': ('7777',)}}}}
}


def flatten_dict_A(y):
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

def flatten_dict_B(root, prefix_keys=True):
    dicts = [([], root)]
    ret = {}
    seen = set()
    for path, d in dicts:
        if id(d) in seen:
            continue
        seen.add(id(d))
        for k, v in d.items():
            new_path = path + [k]
            prefix = '_'.join(new_path) if prefix_keys else k
            if hasattr(v, 'items'):
                dicts.append((new_path, v))
            else:
                ret[prefix] = v
    return ret


pprint(basedict)
pprint(flatten_dict_A(basedict))
pprint(flatten_dict_B(basedict))