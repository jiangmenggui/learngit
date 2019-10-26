#!/env/bash 
# coding=utf-8


def count_time(func):
	def wrapper(*args):
		start = time.time()
		r = func(*args)
		end = time.time()
		return r 
	
	return wrapper

	