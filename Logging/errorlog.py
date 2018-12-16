import logging
x=10
y=0
try:
	z=x/y
except Exception as e:
	logging.exception("Exception occured")