

def sort_0_1_2(params):


	left = 0
	right = len(params)-1
	mid = 0
	
	while mid<=right:
		
		choice = params[mid]
		if choice == 0:
			params[left],params[mid] = params[mid],params[left]
			left = left + 1
			mid = mid + 1
		elif choice == 1:
			params[left],params[mid] = params[mid],params[left]
			mid = mid + 1
		else:

			params[right],params[mid] = params[mid],params[right]
			right = right-1 



params = [0,1,2,0,1,2]

sort_0_1_2(params)
print(params)



