import rdflib
from pprint import pprint

g = rdflib.Graph()
g.load('http://dbpedia.org/resource/Semantic_Web')

pprint([(s,p,o) for s,p,o in g])
