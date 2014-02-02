I had wanted to find a source syntax I could add to Markdown so that when it
was rendered to HTML, it would include RDFa stuff in it. I'm not sure that's
worth the effort, but I started it
[here](https://github.com/wware/redcarpet/tree/wware).

My next thought is to use HTML comments to hide Turtle statements in Markdown
source, and maybe write some code to add to RDFlib that knows how to navigate
a Github repository to find the *.md files, go to their raw source files, and
extract a semantic net based on that. So that's my next idea.

<!--
@prefix dc:   <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
<http://willware.net/#self> a foaf:Person ;
  foaf:name         "Will Ware" ;
  foaf:mbox         <mailto:wware@alum.mit.edu> ;
  foaf:homepage     <http://willware.net/> ;
  foaf:weblog       <http://willware.blogspot.com/> .
-->
