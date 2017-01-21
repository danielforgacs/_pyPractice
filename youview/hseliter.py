import sys
import hou


def get_selection():
    # return hou.selectedNodes()
    return hou.node('/obj/subnet1').allSubChildren()

def gen_selection():
    for node in get_selection():
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
    print(type(selection), len(selection), sys.getsizeof(selection))
    print(type(sel), len(list(sel)), sys.getsizeof(sel))
