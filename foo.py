import rdflib
from StringIO import StringIO
from pprint import pprint

if False:
    g = rdflib.Graph()
    g.load('http://en.openei.org/wiki/Special:ExportRDF/Paris,_France')
    pprint([(s, p, o) for s, p, o in g])

    # THIS WORKS, BUT GITHUB PUTS NOTHING USEFUL IN THIS
    # import rdflib
    # g = rdflib.Graph()
    # g.parse('https://github.com/wware/md-rdfa', format='rdfa')

from BeautifulSoup import BeautifulSoup
import urllib

LOCAL = True

class GithubMdSpider(object):
    def __init__(self):
        self.links = []
        self.visited = set()

    def explore_project(self, username, projectname):
        self.text = ''
        self.explore('/{0}/{1}'.format(username, projectname))
        return StringIO(self.text)

    def open_path(self, path):
        return urllib.urlopen('https://github.com' + path)

    def hack_path(self, path):
        if path.endswith('.md'):
            self.text += self.open_path(path.replace('/blob/', '/raw/')).read()

    def explore(self, path):
        if path in self.visited:
            return
        self.visited.add(path)
        self.links.append(path)
        while self.links:
            path = self.links.pop(0)
            self.hack_path(path)
            soup = BeautifulSoup(self.open_path(path))
            for link in soup.findAll('a'):
                attrs = dict(link.attrs)
                if attrs.get('class') == 'js-directory-link':
                    self.links.append(attrs['href'])


class LocalSpider(object):
    # LAZY: I know what files I'm looking for, spell them out explicitly
    # rather than doing a directory tree traversal. TODO: use os.walk()
    def explore_project(self, name, project):
        r = open('README.md').read()
        r += '\n' + open('more/other.md').read()
        return r


from mdgraph import MarkdownGraph

store = MarkdownGraph()
sp = GithubMdSpider()
#sp = LocalSpider()
store.parse(sp.explore_project('wware', 'md-rdfa'), format="md")
print store.serialize(format="turtle")
