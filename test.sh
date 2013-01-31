#!/bin/sh
virtualenv -p python2.7 .env
.env/bin/pip install -r requirements.txt
.env/bin/python manage.py test test_app