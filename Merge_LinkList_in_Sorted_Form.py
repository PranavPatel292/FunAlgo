array = [4, 138, 183, 422, 925, 5, 319, 349, 566, 676, 866, 4, 163, 253, 393, 548, 4, 60, 89, 203, 344, 6, 346, 356, 434, 522, 719, 842, 10, 32 ,63, 66, 80, 149, 255, 393, 453, 690, 966 ,8 ,187 ,395 ,442 ,526 ,641, 741, 791, 928]

# class MinHeap:
#     def __init__(self, array):
#         # Do not edit the line below.
#         self.heap = self.buildHeap(array)

#     def buildHeap(self, array):
#     	firstChild = (len(array) -2) // 2
#     	for currentIdx in reversed(range(firstChild  + 1)):
#     		self.siftDown(currentIdx, len(array) - 1, array)
#     	return array
		

#     def siftDown(self, currentIdx, endIdx, heap):
#         # Write your code here.
#         childOne = currentIdx * 2 + 1
#         while childOne <= endIdx:
#         	childTwo = currentIdx * 2 +  2 if currentIdx * 2 + 2 <= endIdx else -1
#         	if childTwo != -1 and heap[childTwo] < heap[childOne]:
#         		idxToSwap = childTwo
#         	else:
#         		idxToSwap = childOne
#         	if heap[currentIdx] > heap[idxToSwap]:
#         		self.swap(currentIdx, idxToSwap, heap)
#         		currentIdx = idxToSwap
#         		childOne =  currentIdx * 2 + 1
#         	else:
#         		return

#     def swap(self, idx1, idx2, heap):
#     	heap[idx1], heap[idx2] = heap[idx2], heap[idx1]

#     def siftUp(self, currentIdx, heap):
#     	parentIdx = (currentIdx - 1) // 2

#     	while currentIdx > 0 and heap[parentIdx] > heap[currentIdx]:
#     		self.swap(parentIdx, currentIdx,  heap)
#     		currentIdx = parentIdx
#     		parentIdx = (currentIdx - 1) // 2
        
#     def peek(self):
#         # Write your code here.
#         return self.heap[0]

#     def remove(self):
#     	# (N * k * log(k))

#     	self.swap(0, len(self.heap) - 1, self.heap)
#     	removeValue = self.heap.pop()
#     	self.siftDown(0, len(self.heap) - 1, self.heap)
#     	print(removeValue)

#     def insert(self, value):
#         # Write your code here.
#         self.heap.append(value)
#         self.siftUp(len(self.heap) - 1, self.heap)


# h = MinHeap([])

# counter = 0

# for i in range(len(array)):
# 	MinHeap.insert(h, array[i])
# 	counter += 1
# 	# print(array[i])

# while counter > 0:
# 	MinHeap.remove(h)
# 	counter -= 1

# print("end")

#-------------------------------------------------------------------------------------------------------------------------#

# Feel free to use the navie apporach as well.!

class Node:
	def __init__(self, value):
		self.data = value
		self.next = None

class LinkList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, value):
		if self.head is None:
			self.head = Node(value)
			self.tail = self.head
		else:
			self.tail.next = Node(value)
			self.tail = self.tail.next

	def return_head(self):
		return self.head


# this block of code will create the linklist from the given array

nextElementIdx = 0
i = 0;
question = []
while i < len(array):
	size = array[i]
	temp = size
	l1 = LinkList()
	while temp != 0:
		temp -= 1
		i += 1
		l1.add(array[i])

	question.append(l1.return_head())
	i += 1

# printing of the an array containg the link list: -

# for i in range(len(question)):
# 	head = question[i]
# 	while head:
# 		print(head.data, end="->")
# 		head = head.next
# 	print()

result = None

for i in range(len(question)):
	head = question[i]

	while head:

		if result is None:
			result = Node(head.data)
			head = head.next

		else:
			temp1 = result

			# travel the resulted linklist to find the apporiate postion of the node to be inserted!

			while temp1:

				if temp1.data > head.data:
					add = Node(head.data)
					add.next = temp1
					result = add
					break

				elif temp1.next is None:
					temp1.next = Node(head.data)
					break

				elif temp1.next.data < head.data:
					temp1 = temp1.next

				else:
					# now the logic of moving the element to the palce
					curernt_next = temp1.next
					temp1.next = Node(head.data)
					temp1 = temp1.next
					temp1.next = curernt_next
					break

			head = head.next

# As temp is pointing to the head of the list we will return the temo
print()
print()
while result:
	print(result.data, end="->")
	result = result.next

print()
print()