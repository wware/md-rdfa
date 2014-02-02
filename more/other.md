Here is another Markdown file with some more embedded RDF hidden in an HTML
comment. You won't see that on Github unless you look at the raw MD source.

<!--
@prefix dc:     <http://purl.org/dc/terms/> .
@prefix schema: <http://schema.org/> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
<http://willware.willware.blogspot.com> a schema:WebPage ;
  foaf:author       <http://willware.net/#self> .
-->
