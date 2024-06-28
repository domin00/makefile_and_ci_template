install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	python -m pytest -vv main_test.py

format:
	black *.py 

all: install test format  