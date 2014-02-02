import os
import StringIO

from rdflib import Graph


class MarkdownGraph(Graph):
    def parse(self, *args, **kwargs):
        if kwargs.get('format') == 'md':
            args = list(args)
            source = args.pop(0)
            assert isinstance(source, basestring)
            assert os.path.isfile(source)
            pieces = [part.split('-->')[0] for
                      part in open(source).read().split('<!--')[1:]]
            source = StringIO.StringIO('\n'.join(pieces))
            args = tuple([source] + args)
            kwargs['format'] = 'n3'
        super(MarkdownGraph, self).parse(*args, **kwargs)
