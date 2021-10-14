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
		#check when the list have valid elements
		if(int(i) == i):
			result = result * i
		else:
			return False
	return result
#Driver
list01 = [1, 2, 3, 7]
list02 = [3, 2, 4, 89]

print(multiply_list(list01))
print(multiply_list(list02))





