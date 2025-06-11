.PHONY: test type-check

test:
	pytest -v --cov=agent_mode

type-check:
	mypy agent_mode/

coverage-report:
	coverage html
	open htmlcov/index.html
