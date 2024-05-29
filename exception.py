class Accident(Exception):
	def __init__(self, message):
			self.message = message
		
	def print_exception(self):
		print('User defined exception: ', self.message)


try:
	raise Accident('crash between two cars')

except Accident as e:
	e.print_exception()