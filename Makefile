GIT_COMMIT_MSG = "default commit"


install:
	pip install --upgrade pip && pip install -r requirements.txt
lint:
	pylint --disable=R,C part_1/*.py part_1/samples/*.py
test:
	python3 -m pytest --cache-clear -vv part_1/tests.py

push:
	git add . && git commit -m "$(GIT_COMMIT_MSG)" && git push origin main