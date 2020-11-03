sequences = [10, 345, 2, 1, 43, 2, 5, 2, 1, 7, 3, 25, 7, 4]

for element in sequences:
    if element > 4:
        print(element)

# filter

def my_filter(element):
    return element>4

filetered_result = filter(my_filter, sequences)

print(filetered_result)

print(list(filetered_result))

# ptr on set is empty because of previous operation. like cursor
print(set(filetered_result))

# with lambda

filetered_result = filter(lambda x: x > 4, sequences)

print(list(filetered_result))