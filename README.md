This is an example of Markdown source with some RDFa embedded in it. I wish I had some elegant
source syntax for this, but I don't yet have such a thing, For now there is some pretty ugly
HTML in this source file.

<p xmlns:dc="http://purl.org/dc/elements/1.1/"
   about="http://www.example.com/books/wikinomics">
  In his latest book, <cite property="dc:title">Wikinomics</cite>,
  <span property="dc:creator">Don Tapscott</span> explains deep changes in technology,
  demographics and business. The book is due to be published in
  <span property="dc:date" content="2006-10-01">October 2006</span>.
</p>

The semantic network resulting from the paragraph above appears below in
[Turtle](http://www.w3.org/TeamSubmission/turtle/) format.

```
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.example.com/books/wikinomics> dc:creator "Don Tapscott" ;
    dc:date "2006-10-01" ;
    dc:title "Wikinomics" .
```

The role of "span" and "cite" above appear to be exactly the same. So the important things are the
namespace declarations, the "about" marker, and the spans with properties. Perhaps the same thing
could be done like this.

    [xmlns]: dc="http://purl.org/dc/elements/1.1/"
    [about]: http://www.example.com/books/wikinomics
    In his latest book, {dc:title Wikinomics}, {dc:creator Don Tapscott}
    explains deep changes in technology, demographics and business.
    The book is due to be published in {dc:date 2006-10-01}[October 2006].
    [about]:

So this works in the following way.

* `[xmlns]` is a special Markdown label for establishing a namespace.
* `[about]` indicates that, until the following `[about]`, any RDFa properties take the argument as
  the subject. This is done as a `<span>`. An empty `[about]` indicates that no new about-context
  is starting as the previous one ends.
* Curly braces represent a RDFa property, also done as a `<span>`.
* Curly braces followed immediately by square brackets indicate that the object is different from
  what should appear in the rendered HTML.
* For translation to HTML, all these things can be done in a preprocessing stage, before the normal
  Markdown parser.
* It's easy to write a parser that extracts the semantic net directly from the source.

What I would really like is something that will show correct RDFa on Github. For that, I need to use
this format (call it `*.mdr`) and then do the preprocessing step prior to checkin to get `*.md` files.
This could be done by mirroring a directory structure of documents.