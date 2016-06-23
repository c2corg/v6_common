SITE_PACKAGES = $(shell .build/venv/bin/python -c "import distutils; print(distutils.sysconfig.get_python_lib())" 2> /dev/null)

.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo
	@echo "Main targets:"
	@echo
	@echo "- check			Run linter and tests"
	@echo "- test			Run the tests"
	@echo "- lint			Run flake8 checker on the Python code"
	@echo "- clean			Remove generated files"
	@echo "- cleanall		Remove all the build artefacts"
	@echo "- install		Install and build the project"

.PHONY: clean
clean:
	rm -f .build/dev-requirements.timestamp

.PHONY: cleanall
cleanall: clean
	rm -rf .build

.PHONY: check
check: lint test

.PHONY: lint
lint: .build/venv/bin/flake8
	.build/venv/bin/flake8 c2corg_common

.PHONY: test
test: .build/venv/bin/nosetests .build/requirements.timestamp
	.build/venv/bin/nosetests

.PHONY: install
install: .build/requirements.timestamp

.build/requirements.timestamp: .build/venv requirements.txt
	.build/venv/bin/pip install -r requirements.txt
	touch $@

.build/venv/bin/flake8: .build/dev-requirements.timestamp

.build/venv/bin/nosetests: .build/dev-requirements.timestamp

.build/dev-requirements.timestamp: .build/venv dev-requirements.txt
	.build/venv/bin/pip install -r dev-requirements.txt
	touch $@

.build/venv:
	mkdir -p $(dir $@)
	virtualenv --no-site-packages $@

$(SITE_PACKAGES)/c2corg_common.egg-link: .build/venv requirements.txt setup.py
	.build/venv/bin/pip install -r requirements.txt
