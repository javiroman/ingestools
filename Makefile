.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete
	rm -fr *.egg-info
	find ingestools -name __pycache__ | xargs rm -fr
	rm -fr build dist
	rm -fr __pycache__
	rm -fr .venv


virtualenv:
	virtualenv --prompt '(ingestools) ' .venv
	.venv/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source .venv/bin/activate"
	@echo

install:
	python setup.py install

editable:
	pip install --editable .

test:
	python -m pytest \
		-v \
		--cov=myapp \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t myapp:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel
