#!/bin/sh

export FLASK_APP=app.py
flask run $* >log.txt 2>&1

