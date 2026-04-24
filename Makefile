build-proj:
	sphinx-build -vvv --write-all --fresh-env src build

create-dev:
	pre-commit install
	pre-commit autoupdate
	uv sync
	uv build

serve-site:
	sphinx-autobuild src build
