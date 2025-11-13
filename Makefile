install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall: build
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

format:
	uv run ruff format brain_games

check: lint