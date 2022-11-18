# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
pprint([{'bin':bin(digit), 'dec':digit, 'hex':hex(digit), 'oct':oct(digit)} for digit in range(16)])
