[xmlns]: dc="http://purl.org/dc/elements/1.1/"

This sorta works in a half-baked way. The rendered HTML is full of junk. This could work with a mod to Redcarpet.
---

[about]: http://www.example.com/books/wikinomics
In his latest book, {dc:title Wikinomics}, {dc:creator Don Tapscott}
explains deep changes in technology, demographics and business.
The book is due to be published in {dc:date 2006-10-01}[October 2006].
[about]: end

This hides the junk but introduces stupid paragraph breaks.
---

[about]: http://www.example.com/books/wikinomics
In his latest book,
[property]: dc:title
Wikinomics
[property]: end
,
[property]: dc:creator
Don Tapscott
[property]: end
explains deep changes in technology, demographics and business.
The book is due to be published in
[property]: dc:date=2006-10-01
October 2006
[property]: end
.
[about]: end

Well that is certainly ugly. I was hoping to arrive at something where
Github could render decent-looking HTML while I could easily process the
same source file to extract the semantic net. It would be splendid if
Github would preserve the RDFa in its rendition but no such luck.

Github uses Redcarpet as its Markdown engine, presumably with very few
modifications. Perhaps I can add my curly-brace notation to Redcarpet
and propose it as a pull request, and with luck maybe Github would pick
it up.

The selling point to Github is that developers could easily embed their
own RDFa in any Markdown files they write. That could be used for better
searching of repositories or for giving hints to Google and other search
engines. It could also provide machine-tractable history and commentary
so that a project could identify itself as a fork from another project,
and identify what new direction it explores, and what considerations
the developer is focused on.

When properties are rendered into HTML, they should appear as links to
the object if the object is a URI. If it is a value, just put it in the
HTML as is.
