all: test

test:
	# -s - For std output
	# -B - Dont create byte code
	PYTHONPATH=modules python -B -m pytest -s unittests

testi:
	PYTHONPATH=modules python -m pytest -s unittests
