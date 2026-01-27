build:
	sphinx-build -vvv --write-all --fresh-env src build

create-dev:
	uv sync
	uv build

serve:
	sphinx-autobuild src build
