SRC = $(wildcard ./*.ipynb)

all: markdown_merge docs

markdown_merge: $(SRC)
	nbdev_build_lib
	touch markdown_merge

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
