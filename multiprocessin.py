# import time
# import multiprocessing

# square_result = []

# def calc_square(numbers):
# 	global square_result
# 	for n in numbers:
# 		print('square: ', n*n)

# 	square_result.append(n*n)



# if __name__ == '__main__':
# 	arr = [2,3,8,9]
# 	p1 = multiprocessing.Process(target = calc_square, args = (arr,))

# 	p1.start()

# 	p1.join()
# 	print('result'+str(square_result))


# print('Done')

import threading
import numpy as np
import time

def matrix_multiplication(A, B, result, start_row, end_row):
		for i in range(start_row, end_row):
				for j in range(len(B[0])):
						result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

def multithreading_matrix_multiplication(A, B):
		num_threads = 4
		threads = []
		result = np.zeros((len(A), len(B[0])))
		rows_per_thread = len(A) // num_threads

		for i in range(num_threads):
				start_row = i * rows_per_thread
				end_row = (i + 1) * rows_per_thread if i != num_threads - 1 else len(A)
				thread = threading.Thread(target=matrix_multiplication, args=(A, B, result, start_row, end_row))
				threads.append(thread)
				thread.start()

		for thread in threads:
				thread.join()

		return result

# Example matrices
A = np.random.rand(200, 200)
B = np.random.rand(200, 200)

# Multithreading performance test
start_time = time.time()
result = multithreading_matrix_multiplication(A, B)
end_time = time.time()
print(f"Multithreading time: {end_time - start_time} seconds")


import multiprocessing
import numpy as np
import time

def matrix_multiplication(A, B, result, start_row, end_row):
		for i in range(start_row, end_row):
				for j in range(len(B[0])):
						result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

def multiprocessing_matrix_multiplication(A, B):
		num_processes = 4
		pool = multiprocessing.Pool(processes=num_processes)
		manager = multiprocessing.Manager()
		result = manager.list([np.zeros(len(B[0])) for _ in range(len(A))])
		rows_per_process = len(A) // num_processes
		processes = []

		for i in range(num_processes):
				start_row = i * rows_per_process
				end_row = (i + 1) * rows_per_process if i != num_processes - 1 else len(A)
				process = multiprocessing.Process(target=matrix_multiplication, args=(A, B, result, start_row, end_row))
				processes.append(process)
				process.start()

		for process in processes:
				process.join()

		return np.array(result)

# Example matrices
A = np.random.rand(200, 200)
B = np.random.rand(200, 200)

# Multiprocessing performance test
start_time = time.time()
result = multiprocessing_matrix_multiplication(A, B)
end_time = time.time()
print(f"Multiprocessing time: {end_time - start_time} seconds")
