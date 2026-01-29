a = {2,3,29}
b = {23,45,67}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))
print(len(a))
a.clear()
print(a)