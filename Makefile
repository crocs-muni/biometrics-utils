all: install

lint:
	flake8 --ignore E501

install:
	pip3 install --user -r requirements.txt
	
demo:
	python3 detect_faces.py --verbose --image images/example.jpg
	
demo-legacy:
	python detect_faces.py --verbose --image images/example.jpg
