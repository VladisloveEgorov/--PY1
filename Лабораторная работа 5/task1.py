from pprint import pprint
N = 16
list_ = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(N)]
pprint(list_)
