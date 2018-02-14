#Lesson02 - Assignment3 - Sum Series
#contains 3 methods: fibonacci, lucas and sum_series
#code which tests the methods in the "main" method

#fibonacci - which returns the fibonacci number for the input number
#starting values - fibonacci(0)=0, fibonacci(1)=1
#any other fibonacci number value is the sum of the previous 2 fibonacci values(numbers)
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return (fibonacci(n-1) + fibonacci(n-2))

#lucas - which returns the lucas number for the input number
#starting values - lucas(0) =2, lucas(1)=1
#any other lucas number value is the sum of the previous 2 lucas numbers(values)
def lucas(n):
	if n == 0:
		return 2
	if n == 1:
		return 1
	return (lucas(n-1) + lucas(n-2))

#sum_series - with 3 input params 
	#n - value for which we need to compute fibonacci value or lucas value
	#x - with a default value 0
	#y - with a default value 1
#if x and y have the default values, then return the Fibonacci number for the input value
#if x and y have the values 2 and 1 respectively, then return the Lucas number for the input value
#if x and y have any other value, then return -1
def sum_series(n,x=0,y=1):
	if x == 0 and y == 1:
		return (fibonacci(n))
	elif x == 2 and y == 1:
		return (lucas(n))
	else: return -1


#testing code in main block
if __name__ == "__main__":
	print ("Running tests")

	assert(sum_series(0) == 0) #fibonacci series value for 0
	assert(sum_series(0,0,1) == 0) #fibonacci series value for 0
	assert(sum_series(0,2,1) == 2) #lucas series value for 0
	assert(sum_series(0,1,1) == -1) #not fibonacci or lucas series

	assert(sum_series(1) == 1) #fibonacci series value for 1
	assert(sum_series(1,0,1) == 1) #fibonacci series value for 1
	assert(sum_series(1,2,1) == 1) #lucas series value for 1
	assert(sum_series(1,1,1) == -1) #not fibonacci or lucas series

	assert(sum_series(4) == 3) #fibonacci series value for 4
	assert(sum_series(4,0,1) == 3) #fibonacci series value for 4
	assert(sum_series(4,2,1) == 7) #lucas series value for 4
	assert(sum_series(4,1,1) == -1) #not fibonacci or lucas series

	assert (sum_series(10) == 55) #fibonacci series value for 10
	assert (sum_series(10,0,1) == 55) #fibonacci series value for 10
	assert(sum_series(10,2,1) == 123) #lucas series value for 10
	assert(sum_series(10,1,1) == -1) #not fibonacci or lucas series

	assert (sum_series(20) == 6765) #fibonacci series value for 20
	assert (sum_series(20,0,1) == 6765) #fibonacci series value for 20
	assert(sum_series(20,2,1) == 15127) #lucas series value for 20
	assert(sum_series(20,1,1) == -1) #not fibonacci or lucas series

	print ("Tests passed")
