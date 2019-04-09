def max_list_iter(int_list):
    if int_list == None:
        raise ValueError
    elif not int_list:
        return None
    largest = int_list[0]
    for i in int_list:
        if i > largest:
            largest = i
    return largest
   # must use iteration not recursion
   #finds the max of a list of numbers and returns the value (not the index)
   #If int_list is empty, returns None. If list is None, raises ValueError"""

def reverse_rec(int_list):   # must use recursion
    if int_list == None:
       raise ValueError
    elif len(int_list) == 0:
        return int_list
    sliced = reverse_rec(int_list[:-1])
    return int_list[-1:] + sliced
   #recursively reverses a list of numbers and returns the reversed list
   #If list is None, raises ValueError

def bin_search(target, low, high, int_list):
	if not int_list or low > high:
	   return None
	elif int_list == None:
	   raise ValueError
	middle = (low+high)//2
	if target == int_list[middle]:
		return middle
	elif target < int_list[middle]:
		return bin_search(target, low, middle-1, int_list)
	elif target > int_list[middle]:
		return bin_search(target, middle+1, high, int_list)
   #searches for target in int_list[low..high] and returns index if found
   #If target is not found returns None. If list is None, raises ValueError

