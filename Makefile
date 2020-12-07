make style:
	flake8 src

make types:
	python -m mypy src

make test:
	python -m pytest src

make check:
	make style types test
