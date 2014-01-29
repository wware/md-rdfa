#!/bin/sh

if [ ! -d venv ]
then
    virtualenv venv
fi

source venv/bin/activate

if [ ! -f venv/bin/rdf2dot ]
then
    pip install rdflib
fi

python hack.py README.md
