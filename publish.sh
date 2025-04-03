#!/bin/bash

. "$1"/bin/activate
python -m build
python -m twine upload $2 dist/*
