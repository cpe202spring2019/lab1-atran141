
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
   pass
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
