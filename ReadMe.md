
# libSDL3 usable in Python Language via ctypes binding

## Install instructions

```shell
# create ".venv" hidden directory if missing and activate it
python -m venv .venv

# "pip install" in virtual environment for requirements
pip install -r requirements.txt
```

## Launching apps

### 1. activate venv

In BASH ( Debian or MSYS+Windows tested )

```bash
source .venv/bin/activate # or : source .venv/Scripts/activate
```

In VSCode should be activated by default because of standard naming ( ".venv" name ) when opening the directory

### 2. run ".py" scripts with "python"

```shell

# a simple start ( from scratch )
python sdl3-simple.py

# example from binding repository
# ( repository : https://github.com/Aermoss/PySDL3 )
python sdl3-example.py
```
