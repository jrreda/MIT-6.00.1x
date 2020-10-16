import math

def polysum(n, s):
    '''
    A regular polygon has 'n' number of sides. Each side has length 's'
    it returns the sum, rounded to 4 decimal places.
    '''
    area = (0.25*n*math.sqrt(s)) / math.tan(math.pi /n)
    perimeter = n*s
    return round(area + perimeter**2 ,4)