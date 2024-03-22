format:
	ruff check --fix

isort:
	isort .

format_all: isort format

load_lyrics:
	python scripts/get_lyrics.py