#empty list
numList = []

#result of multiplying the elements in list 
result = 0

#function for multiplying all elements in list
def multiply_list(numList):
	'''
	Multiplying all elements in list

	This function is simply multiplying all elements in list

	Parameter
	---------
	numList: list
		list for multiplying all elements
	
	Return
	------
	int 
		The multiple of all element in list

	Examples
	--------
	>>>multiply_list([1,2,3])
	6
	>>>multiply_list([3,4,7])
	84
	'''
	result = 1
	for i in numList:
		result = result * i
	#show the result when the list have valid inputs
	if(isinstance(result, int)):
		return result
	else:
		return False
#Driver
list01 = [1, 2, 3, 7]
list02 = [3, 2, 4, 89]

print(multiply_list(list01))
print(multiply_list(list02))





