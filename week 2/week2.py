def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    counter = 1
    while exp <= 0:
    	counter *= base 
    	exp -= 1
    return base

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 1:
    	return base
    else:
    	return base * recurPower(base, exp -1)

def printMove(fr, to):
	print('movefrom ' + str(fr) + ' to '+ str(to))
def Towers(n, fr, to, spare):
	if n== 1:
		printMove(fr, to)
	else:
		Towers(n-1, fr, spare, to)
		Towers(1, fr, to, spare)
		Towers(n-1, spare, to, fr)

'''that implements this idea. One easy way to do this is to begin with a test value equal to the smaller
  of the two input arguments,and iteratively reduce this test value by 1 until you either 
  reach a case where the test divides both a and b without remainder, or you reach 1.
  '''

def gcdIter(a, b):
	'''
	a, b: positive integers
	returns: a positive integer, the greatest common divisor of a & b.
	'''
    if a < b:
        test_value = a
    else:
        test_value = b
    for n in range(test_value):
        if a/test_value == a//test_value and b/test_value == b//test_value:
            return test_value
            break
        elif test_value == 1:
            return 1
            break
        else:
            test_value -= 1

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
    	return 
    else:
    	return gcdRecur(b, a%b)

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    def toAlphabet(aStr):
        aStr = aStr.lower()
        ans = ''
        for char in aStr:
            if char in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + char
        return ans
    def is_In(char, aStr):
        if len(aStr) == 0 or (len(aStr) == 1 and char != aStr):
            return False
        elif aStr[len(aStr) // 2] == char:
            return True
        elif aStr[len(aStr) // 2] < char:
            return is_In(char, aStr[:len(aStr) // 2])
        else:
            return is_In(char, aStr[len(aStr) // 2:])
    return(is_In(char, toAlphabet(aStr)))

def inString(s):
	s = s.lower()
	ans =''
	for char in s:
		ans += char
	return ans

#True
def isIn(char, aStr):

    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    bisect = aStr[len(aStr)//2]
    if bisect == char:
        return True
    elif bisect > char:
        return isIn(char, aStr[:len(aStr)//2])
    else:
        return isIn(char, aStr[len(aStr)//2:])
print(isIn('e',"Hello, Kitte!"))

### Final