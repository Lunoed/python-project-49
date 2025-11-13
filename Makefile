install:
	uv sync

lint:
	uv run ruff check brain_games

build:
	uv build

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

package-install:
	uv tool install dist/*.whl
