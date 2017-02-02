clean:
	@find . -name '*.pyc' -delete

profile: clean
	@NUMBER=1000000 pypy -m cProfile collatz.py

test: clean
	@pypy -m unittest discover

run: clean
	@time NUMBER=1000000 pypy "collatz.py"