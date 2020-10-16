def get_data(aTuple):
    nums= ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return(min_nums, max_nums, unique_words)

(small, large, words) = get_data(((1,'mine'),
                                  (3, 'yours'),
                                  (5, 'ours'),
                                  (7, 'mine')))

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    conc_aTup = ()
    for t in range(len(aTup)):
    	if t % 2 == 0:
    		conc_aTup += (aTup[t],)
    return conc_aTup
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))

#one line problem 
def oddTuples(aTup):
    return (aTup)[ : : 2]

#Swap in Lists
x, y = 0, 1

L = [x, y]
print(L)
L[x], L[y] = L[y], L[x]
print(L)

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    total_values = 0
    for value in aDict.values():
        total_values += len(value)
    return total_values

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    largest = 0
    for value in aDict.values():
        if len(value) > largest:
            largest = len(value)
    for key in aDict.keys():
        if len(aDict[key]) == largest:
                return key