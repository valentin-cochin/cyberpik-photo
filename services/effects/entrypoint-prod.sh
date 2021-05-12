#!/bin/sh

echo "Application is gonna be launched with gunicorn..."

gunicorn -b 0.0.0.0:5000 manage:app
