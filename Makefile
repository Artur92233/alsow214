PHONY: test
test:
	@echo 'tests started . . .'
	pytest . -v



PHONY: check
check: test
	black .
	isort .
	flake8 .
