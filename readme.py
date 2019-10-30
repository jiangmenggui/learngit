#!/env/bash 
# coding=utf-8


def count_time(func):
	def wrapper(*args):
		start = time.time()
		r = func(*args)
		end = time.time()
		return r 
	
	return wrapper


def func(n):
	s = 0 
	for i in range(1,n+1):
		s += i 
	return s 

if __name__ == "__main__":
<<<<<<< HEAD
	func(100)
	pass

=======
    func(100)
    100
>>>>>>> dev
