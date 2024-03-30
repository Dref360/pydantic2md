.PHONY: lint
lint:
	ruff check
.PHONY: test
test: lint
	poetry run pytest tests --cov=pydantic2md

.PHONY: format
format:
	poetry run ruff format

.PHONY: mypy
mypy:
	poetry run mypy --show-error-codes pydantic2md