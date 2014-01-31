import os
import sys
import StringIO

from rdflib import Graph, Literal, BNode, RDF
from rdflib.namespace import FOAF, DC

if __name__=='__main__':

    store = Graph()
    x = [part.split('-->')[0] for
         part in open(sys.argv[1]).read().split('<!--')[1:]]
    store.parse(StringIO.StringIO('\n'.join(x)), format="turtle")

    print store.serialize(format="pretty-xml")
    print store.serialize(format="turtle")
