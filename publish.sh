#!/bin/bash

. "$1"/bin/activate
export TWINE_USERNAME="__token__"
python -m build
python -m twine upload $2 dist/*
