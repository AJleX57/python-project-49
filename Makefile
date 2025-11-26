test:
	uv run pytest

test-coverage:
	uv run pytest --cov=brain_games --cov-report=xml

lint:
	uv run ruff check brain_games

format:
	uv run ruff format brain_games

install:
	uv sync

build:
	uv build

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl

reinstall: build
	uv tool install --force dist/*.whl
