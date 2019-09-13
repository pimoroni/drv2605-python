LIBRARY_VERSION=$(shell cat library/setup.py | grep version | awk -F"'" '{print $$2}')
LIBRARY_NAME=$(shell cat library/setup.py | grep name | awk -F"'" '{print $$2}')

.PHONY: usage install uninstall
usage:
	@echo "Library: ${LIBRARY_NAME}"
	@echo "Version: ${LIBRARY_VERSION}\n"
	@echo "Usage: make <target>, where target is one of:\n"
	@echo "install:       install the library locally from source"
	@echo "uninstall:     uninstall the local library"
	@echo "check:         peform basic integrity checks on the codebase"
	@echo "python-readme: generate library/README.rst from README.md"
	@echo "python-wheels: build python .whl files for distribution"
	@echo "python-sdist:  build python source distribution"
	@echo "python-clean:  clean python build and dist directories"
	@echo "python-dist:   build all python distribution files"
	@echo "python-testdeploy: build all and deploy to test PyPi"
	@echo "tag:           tag the repository with the current version"

install:
	./install.sh

uninstall:
	./uninstall.sh

check:
	@echo "Checking for trailing whitespace"
	@! grep -IUrn --color "[[:blank:]]$$" --exclude-dir=sphinx --exclude-dir=.tox --exclude-dir=.git --exclude=PKG-INFO
	@echo "Checking for DOS line-endings"
	@! grep -IUrn --color "" --exclude-dir=sphinx --exclude-dir=.tox --exclude-dir=.git --exclude=Makefile
	@echo "Checking library/CHANGELOG.txt"
	@cat library/CHANGELOG.txt | grep ^${LIBRARY_VERSION}
	@echo "Checking library/${LIBRARY_NAME}/__init__.py"
	@cat library/${LIBRARY_NAME}/__init__.py | grep "^__version__ = '${LIBRARY_VERSION}'"

tag:
	git tag -a "v${LIBRARY_VERSION}" -m "Version ${LIBRARY_VERSION}"

python-readme: library/README.rst

python-license: library/LICENSE.txt

library/README.rst: README.md
	pandoc --from=markdown --to=rst -o library/README.rst README.md

library/LICENSE.txt: LICENSE
	cp LICENSE library/LICENSE.txt

python-wheels: python-readme python-license
	cd library; python3 setup.py bdist_wheel
	cd library; python setup.py bdist_wheel

python-sdist: python-readme python-license
	cd library; python setup.py sdist

python-clean:
	-rm -r library/dist
	-rm -r library/build
	-rm -r library/*.egg-info

python-dist: python-clean python-wheels python-sdist
	ls library/dist

python-testdeploy: python-dist
	twine upload --repository-url https://test.pypi.org/legacy/ library/dist/*

python-deploy: check python-dist
	twine upload library/dist/*
