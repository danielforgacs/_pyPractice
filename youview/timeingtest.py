# import timeit
import hou
import time

def create_test_scene():
    hou.hipFile.clear(suppress_save_prompt=True)
    rootnode = hou.node('/obj').createNode('subnet')
    rootnode.setDisplayFlag(False)

    for k in range(10000):
        rootnode.createNode('geo')

    return rootnode


def get_selection_list():
    rootnode = create_test_scene()
    selection = rootnode.allSubChildren()

    return selection


def get_selection_generator():
    rootnode = create_test_scene()

    for node in rootnode.allSubChildren():
        yield node


def get_node_names_string():
    # nodes = get_selection_list()
    nodes = get_selection_generator()
    names = [node.name() for node in nodes]
    # names = ''

    # for node in nodes:
    #     names += node.name()

    return names


def main():
    starttime = time.clock()
    names = get_node_names_string()
    elapsedtime = time.clock() - starttime

    print(elapsedtime)
# if __name__ == '__main__':
    # timeit.timeit(get_node_names_string)
#     pass
#     print('OUHKJH')
# import timeit
# print(timeit.timeit("timeingtest.get_node_names_string()",
#         setup="import timeingtest"))
