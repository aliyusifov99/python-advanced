import time


def time_it(func):

	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f'Time taken: {(end - start)*1000}')
		return result

	return wrapper


@time_it
def calc_square(numbers):
	result = []
	for number in numbers:
		result.append(number * number)
	return result


@time_it
def calc_cube(numbers):
	result = []
	for number in numbers:
		result.append(number * number * number)

	return result

arr = range(1,1000000)
calc_cube(arr)
calc_square(arr)