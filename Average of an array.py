# Python3 code to calculate 
# average of array elements 

# Function that return 
# average of an array. 
def average( b , m ): 

	# Find sum of array element 
	sum = 0
	for i in range(m): 
		sum += b[i] 
	
	return sum/m; 

# array 
arr = [10, 2, 3, 4, 5, 6, 7, 8, 9] 
m = len(arr) 
print("The average of the array is:",average(arr, m)) 

# by aditya

