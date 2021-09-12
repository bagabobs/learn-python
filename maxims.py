from pprint import pprint

a = [5, 6, 7, 9, 10]
b = [7, 8, 9, 10, 11]
c = [8, 9, 2, 3, 1]

maxims = map(lambda n: max(*n), zip(a, b, c))
pprint(list(maxims))
