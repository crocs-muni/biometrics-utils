all: install

lint:
	flake8 --ignore E501

install:
	pip install --user -r requirements.txt
