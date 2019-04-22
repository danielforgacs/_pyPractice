import os
# from xml import etree
from xml.etree import ElementTree


XMLFILE = '/home/ford/Documents/dev/pyLearn/xml/data.xml'

class XMLDoc:
    def __init__(self, xmlfile):
        assert os.path.isfile(xmlfile)

        xmltree = ElementTree.parse(xmlfile)
        print(type(xmltree))
        print(dir(xmltree))
        treeroot = xmltree.getroot()
        print(type(treeroot))
        print(dir(treeroot))
        print(treeroot.tag)

        print(len(treeroot))


if __name__ == '__main__':
    xmldoc = XMLDoc(xmlfile=XMLFILE)
