#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

echo "Server is running.." 
echo "http://127.0.0.1:5000/api/data"
