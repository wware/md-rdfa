import sys
import StringIO
from rdflib.plugins.parsers.pyRdfa import pyRdfa

class MarkdownFile(pyRdfa):
    def _get_input(self, filename):
        text = open(filename).read()
        text = ''.join([v for u, v in enumerate(text.split("`")) if (u & 1) == 0])
        return StringIO.StringIO("<html>{0}</html>".format(text))

print MarkdownFile().rdf_from_source(sys.argv[1])
