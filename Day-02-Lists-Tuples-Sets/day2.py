# List
scores = [85, 92, 78, 95, 88]
print("Original List:", scores)

# Access Items
print("\nAccessing Elements")
print(scores[0])
print(scores[3])

# Slicing
print("\nList Slicing")
print(scores[1:4])

# Append
scores.append(91)
print("\nAfter Append")
print(scores)

# Remove
scores.remove(78)
print("\nAfter Remove")
print(scores)

# Sort
scores.sort()
print("\nSorted List")
print(scores)

# Length
print("\nLength")
print(len(scores))

# List Comprehension
numbers = [1, 2, 3, 4, 5]
square = [x ** 2 for x in numbers]
print("\nSquares")
print(square)

# Conditional List Comprehension
high_scores = [x for x in scores if x > 85]
print("\nHigh Scores")
print(high_scores)

# Tuple
coordinates = (10.5, 20.3)
print("\nTuple")
print(coordinates)

# Set
unique_numbers = {1, 2, 2, 3, 3, 4}
print("\nSet")
print(unique_numbers)

# Set Operations
A = {1, 2, 3}
B = {3, 4, 5}

print("\nUnion")
print(A.union(B))

print("\nIntersection")
print(A.intersection(B))

print("\nDifference")
print(A.difference(B))
