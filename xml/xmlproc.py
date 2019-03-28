import os
# from xml import etree
from xml.etree import ElementTree


XMLFILE = '/home/ford/Documents/dev/pyLearn/xml/data.xml'

class XMLDoc:
    def __init__(self, xmlfile):
        assert os.path.isfile(xmlfile)

        xmltree = ElementTree.parse(xmlfile)
        print(dir(xmltree))


if __name__ == '__main__':
    xmldoc = XMLDoc(xmlfile=XMLFILE)
