import rdflib
from pprint import pprint

g = rdflib.Graph()
g.load('http://dbpedia.org/resource/Semantic_Web')

pprint([(s, p, o) for s, p, o in g])

# THIS WORKS, BUT GITHUB PUTS NOTHING USEFUL IN THIS
# import rdflib
# g = rdflib.Graph()
# g.parse('https://github.com/wware/md-rdfa', format='rdfa')
