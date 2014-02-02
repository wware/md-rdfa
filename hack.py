import sys

from mdgraph import MarkdownGraph

if __name__ == '__main__':

    store = MarkdownGraph()
    store.parse(sys.argv[1], format="md")

    print store.serialize(format="pretty-xml")
    print store.serialize(format="turtle")
