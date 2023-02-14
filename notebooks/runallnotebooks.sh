#!/bin/sh
# script to run all notebooks modified
jupyter nbconvert --to script *.ipynb
find .  -name '*.py' -exec sh -c 'python "$1" > "$1.out"' _ {} \;
