def flatten_dict(root, prefix_keys=True):
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


a = {
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

from pprint import pprint
pprint( flatten_dict(a))