a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 9]]
d = [2, 2]
e = [3, 3]
c = [[sum(i * j for i, j in zip(r, x)) for x in zip(*b)] for r in a]
print(c)
# c = [[sum(i * j for i, j in zip(f, e)) for f in zip(*d)]]
# print(c)
# c = [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]
# print(c)
# for b in zip(*a):
#     print(b)

