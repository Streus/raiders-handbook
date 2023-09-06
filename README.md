# Raider's Handbook

This is your one-stop-shop for information about raid training in Guild Wars 2.

## Building
Setup virtual environment.
```sh
# in project root
$ python -m venv .venv
$ source .venv/bin/activate
# or
$ .\\.venv\\Scripts\\Activate.ps1
```

Install packages.
```sh
python -m pip install sphinx sphinx-favicon furo
```

Build HTML.
```sh
$ ./docs/make html
# or
$ .\\docs\\make.bat html
```
