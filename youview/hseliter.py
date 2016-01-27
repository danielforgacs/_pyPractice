import hou


def get_selection():
    return hou.selectedNodes()

def gen_selection():
    for node in get_selection():
        yield node

def main():
    print('\n' + '/|\\'*25)
    selection = get_selection()
    sel = gen_selection()

    print('normal: ' + ' '.join([str(k) for k in selection]))
    print('generator: ' + ' '.join([str(k) for k in sel]))
    print(type(selection))
    print(type(sel))
