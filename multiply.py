#empty list
numList = []
#get size of list
getElements = int(input("Enter number of elements: "))
#value of checking for invalid value input
ch = True
#result of multiplying the elements in list 
result = 0
#function of get elements in list
def check(getElements):
	'''
	Check and add inputs to list.
	This function is simply checking whether inputs are valid or not. If the inputs are valid, inputs can put in list.
	If the inputs are not valid, then exit.

	Parameters
	----------
	getElements: int
		Users input

	Return
	------
	Boolean
		True: list is valid, False: list is invalid
	
	Example
	-------
	>>>check(1)
	True
	>>>check(w)
	False
	'''
	#loop for getting elements in list
	for i in range(0, getElements):
		num = input()
		#block for testing whether inputs are int or not
		try:
			num = int(num)
			numList.append(num)
		#block for get out function when input is not int
		except ValueError:
			print("This is not number")
			return False
	return True
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
	return result

ch = check(getElements)

#show the result when the list have valid inputs
if ch == True:
	result = multiply_list(numList)
	print(result)
elif ch == False:
	print("Invalid value")




