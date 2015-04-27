all: *.cpp *.h *.py
	@python setup.py build
	@mv build/lib.*/my_booster.so .
	@rm -rf build
	
	
