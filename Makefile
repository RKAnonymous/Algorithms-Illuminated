COMMIT_MSG = default commit


install:
	pip install --upgrade pip && pip install -r requirements.txt
lint:
	pylint --disable=R,C part_1/*.py part_1/samples/*.py
test:
	python3 -m pytest --cache-clear -vv part_1/tests.py
format:
	# No need to format the code for now, PyCharm IDE deals with this
	#black *.py mylib/*.py tests/*.py
run:
	#pass
build:
	#pass
push:
	git add . && git commit -m "$(COMMIT_MSG)" && git push origin main