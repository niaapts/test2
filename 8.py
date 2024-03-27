import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')
logging.debug('Start of program')

def factorial(n):
	logging.debug('Start of factorial(%s)' % (n)) 
	total = 1
	for i in range(n + 1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
	logging.debug('End of factorial(%s)' % (n))
	return total
logging.debug('Call of the function')

print(factorial(5))

import pdb
def addition(a, b):
	answer = a * b
	return answer
pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)