#!/bin/bash
sudo apt install python3-flask
sudo apt install python3-flask-cors
python -m venv devops
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
