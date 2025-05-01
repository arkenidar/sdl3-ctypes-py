
# setup
rm -rf .venv
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# start
python sdl3-simple.py
