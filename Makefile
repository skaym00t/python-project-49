install:
	poetry insatll
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user /home/skaym00t/python-project-49/dist/hexlet_code-0.1.0-py3-none-any.whl