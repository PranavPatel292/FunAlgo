# moving the array clock wise with constant space and time complxity n^2:

arr = [1, 2, 3, 4]

for i in range(0, len(arr)):
	for j in range(0, len(arr)):
		index = int((i + j) % len(arr))
		print(arr[index], end="")
	print()

# Explanation: 

# let's say array(arr) is: - [1, 2, 3, 4]
# so, for the first pass of the outer for loop: -
# i = 0
#		j = 0
#			index = int((0 + 0) % 4) = 0
#			print(arr[0])
#		j = 1
#			index = int((0 + 1) % 4) = 1
#			print(arr[1])
#		j = 2
#			index = int((0 + 2) % 4) = 2
#			print(arr[0])
#		j = 3
#			index = int((0 + 3) % 4) = 3
#			print(arr[0])

# i = 1
#		j = 0
#			index = int((1 + 0) % 4) = 1
#			print(arr[0])
#		j = 1
#			index = int((1 + 1) % 4) = 2
#			print(arr[1])
#		j = 2
#			index = int((1 + 2) % 4) = 3
#			print(arr[0])
#		j = 3
#			index = int((1 + 3) % 4) = 0
#			print(arr[0])

# i = 2
#		j = 0
#			index = int((2+ 0) % 4) = 2
#			print(arr[0])
#		j = 1
#			index = int((2 + 1) % 4) = 3
#			print(arr[1])
#		j = 2
#			index = int((2 + 2) % 4) = 0
#			print(arr[0])
#		j = 3
#			index = int((2 + 3) % 4) = 1
#			print(arr[0])

# i = 3
#		j = 0
#			index = int((3 + 0) % 4) = 3
#			print(arr[0])
#		j = 1
#			index = int((3 + 1) % 4) = 0
#			print(arr[1])
#		j = 2
#			index = int((3 + 2) % 4) = 1
#			print(arr[0])
#		j = 3
#			index = int((3 + 3) % 4) = 2
#			print(arr[0])