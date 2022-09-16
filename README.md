# 212-music

## virtual environment -- mac
python3 -m venv env
source env/bin/activate
pip install flask

## virtual environment -- windows
py -m venv env
env\Scripts\activate.bat
pip install flask

## running flask -- mac
source env/bin/activate
export FLASK_APP=run.py
export FLASK_DEBUG=1
flask run

## running flask -- windows
env\Scripts\activate.bat
set FLASK_APP=run.py
set FLASK_DEBUG=1
py -m flask run
 
