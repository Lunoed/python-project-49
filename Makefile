install:
	uv sync

lint:
	uv run ruff check

build:
	uv build

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl
