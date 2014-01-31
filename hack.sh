#!/bin/bash

if [ ! -d venv ]
then
    virtualenv venv
fi

source venv/bin/activate

if [ ! -f .reqs_done ]
then
    pip install -r requirements.txt && touch .reqs_done
fi

python hack.py README.md
