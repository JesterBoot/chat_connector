check-env-file:
	@if [ -f .env ]; then \
        if grep -q 'TG_TOKEN=' .env && grep -q 'DS_TOKEN=' .env && grep -q 'BOT_TYPE=' .env; then \
            echo ".env file is complete"; \
        fi \
    else \
        echo ".env file not found. Creating .env from .env.example..."; \
        cp .env.example .env; \
        echo ".env file created successfully"; \
    fi

run:
	make check-env-file
	python main.py

test:
	poetry run pytest

isort:
	poetry run isort .

mypy:
	poetry run mypy .

black:
	poetry run black . --exclude tests

lint:
	poetry run black --check . --exclude tests
	poetry run isort --check .

