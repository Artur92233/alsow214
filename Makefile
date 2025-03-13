PHONY: test
test:
	@echo 'tests started...'
	@set PYTHONPATH=. && python -m pytest -v -s


PHONY: check
check:
	black .
	isort .
	flake8 .
