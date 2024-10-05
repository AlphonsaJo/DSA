class QueueUsingStacks:
	def __init__(self):
    	# Initialize two stacks
    	self.stack1 = []  # This stack will be used for enqueue operations
    	self.stack2 = []  # This stack will be used for dequeue operations

	def enqueue(self, item):
    	"""
    	Enqueue operation: Push the new item onto stack1.
    	This operation is straightforward and only involves appending the item to stack1.
    	"""
    	self.stack1.append(item)
    	print(f"Enqueued {item}: stack1 = {self.stack1}")

	def dequeue(self):
    	"""
    	Dequeue operation: Remove and return the front item from the queue.
    	To maintain the queue's FIFO order using two stacks:
    	1. If stack2 is empty, pop all items from stack1 and push them onto stack2.
    	2. Pop the top item from stack2, which is the front item of the queue.
    	"""
    	# If stack2 is empty, we need to move elements from stack1 to stack2
    	if not self.stack2:
        	while self.stack1:
            	popped_item = self.stack1.pop()  # Pop from stack1
            	self.stack2.append(popped_item)  # Push onto stack2
        	print(f"Moved stack1 to stack2: stack2 = {self.stack2}")

    	# If stack2 is still empty after transferring, the queue is empty
    	if not self.stack2:
        	print("Queue is empty, cannot dequeue.")
        	return None

    	# Pop the front item from stack2
    	return self.stack2.pop()

	def peek(self):
    	"""
    	Peek operation: Return the front item of the queue without removing it.
    	It works similarly to dequeue, but we just return the top item of stack2 without popping it.
    	"""
    	if not self.stack2:
        	while self.stack1:
            	self.stack2.append(self.stack1.pop())
        	print(f"Moved stack1 to stack2 for peek: stack2 = {self.stack2}")

    	if not self.stack2:
        	print("Queue is empty, cannot peek.")
        	return None

    	return self.stack2[-1]  # Return the top element from stack2 without removing it

	def is_empty(self):
    	"""
    	Check if the queue is empty.
    	The queue is empty only if both stacks are empty.
    	"""
    	return len(self.stack1) == 0 and len(self.stack2) == 0




