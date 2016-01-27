import sys
import hou


def get_selection():
    return hou.selectedNodes()

def gen_selection():
    for node in hou.selectedNodes():
        yield node

def main():
    print('\n' + '/|\\'*25)
    selection = get_selection()
    sel = gen_selection()

    s1 = ' '.join([str(k) for k in selection])
    s2 = ' '.join([str(k) for k in sel])

    print(s1 == s2)
    # print(s1)
    # print(s2)
    print(type(selection), sys.getsizeof(selection))
    print(type(sel), sys.getsizeof(sel))
