# Tuples 
a = (2,3,4,5,6,7,8)

print(a)
print(a[1])

# a[1] = 62 # TypeError: 'tuple' object does not support item assignment

b =(3,) # Single element looks like
c = (5) # This a integer not tuple
print(b)
print(c)
print(type (b))
print(type (c))

# why we use Tuple
# 1. Tuple is faster then list
# 2. Used as dictionary key
# 3. Safe from unintended modifications