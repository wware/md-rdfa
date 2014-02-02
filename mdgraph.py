import os
import StringIO

from rdflib import Graph


class MarkdownGraph(Graph):
    def parse(self, *args, **kwargs):
        if kwargs.get('format') == 'md':
            args = list(args)
            source = args.pop(0)
            if isinstance(source, StringIO.StringIO):
                source = source.read()
            elif isinstance(source, basestring):
                if os.path.isfile(source):
                    source = open(source).read()
            else:
                raise Exception('weird source? {0}'.format(source))
            pieces = [part.split('-->')[0] for
                      part in source.split('<!--')[1:]]
            source = StringIO.StringIO('\n'.join(pieces))
            args = tuple([source] + args)
            kwargs['format'] = 'n3'
        super(MarkdownGraph, self).parse(*args, **kwargs)
