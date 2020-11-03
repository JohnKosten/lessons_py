sequences = [10, 345, 2, 1, 43, 2, 5, 2, 1, 7, 3, 25, 7, 4]
# TODO sequences power 2

result = map(lambda x:x*x, sequences)

print(type(result))

print(list(result))
print(set(result))