class node:

	def __init__(self, val, next_node = None):
		self.val = val
		self.next_node = next_node

class operations:

	def isEmpty(self):
		if (self.front is None) & (self.rear is None):
			return 1
	
	def print(self):
		if self.isEmpty():
			print('Queue is empty.')
		else:
			itr = self.front
			print_queue = ''
			while itr:
				print_queue = print_queue + ' ' + str(itr.val)
				itr = itr.next_node
			print('The queue is: {}'.format(print_queue))

	def peek(self):
		if self.isEmpty():
			print('Queue is empty.')
		else:
			print('The front of the queue is: {}'.format(self.front.val))

class simple_queue(operations):

	def __init__(self):
		self.front = None
		self.rear = None

	def enqueue(self, val):
		if self.isEmpty():
			self.front = node(val)
			self.rear = self.front
		else:
			new_node = node(val)
			self.rear.next_node = new_node
			self.rear = new_node
		print('Element {} inserted in queue.'.format(val))

	def dequeue(self):
		if self.isEmpty():
			print('Queue is empty.')
		else:
			tmp = self.front
			if self.front == self.rear:			
				self.front, self.rear = None, None
			else:
				self.front = self.front.next_node
			print('One element with value {} removed from front.'.format(tmp.val))

class circular_queue(operations):

	q_len = 0

	def __init__(self, size):
		self.front = None
		self.rear = None
		self.MAX_SIZE = size

	def isFull(self):
		if circular_queue.q_len >= self.MAX_SIZE:
			return 1

	def print(self):
		if self.isEmpty():
			print('Queue is empty.')
		else:
			itr = self.front
			print_queue = ''
			while itr != self.rear:
				print_queue = print_queue + ' ' + str(itr.val)
				itr = itr.next_node
			print_queue = print_queue + ' ' + str(self.rear.val)
			print('The queue is: {}'.format(print_queue))

	def enqueue(self, val):
		if self.isEmpty():
			self.front = node(val)
			self.rear = self.front
		else:
			if self.isFull():
				valid_flag = 0
				while valid_flag == 0:
					inp = input('Queue is full. Enqueue will overwrite the front queue element. Continue?(y/n): ')
					switcher = {'y':1, 'n':0}
					found = switcher.get(inp, -1)
					if found != -1:
						valid_flag = 1
						if found == 0:
							return
						else:
							self.front.val = val
							self.rear.next_node = self.front
							self.rear = self.rear.next_node
							self.front = self.front.next_node
					else:
						print('Enter a valid option.')
			else: 				
				new_node = node(val)
				self.rear.next_node = new_node
				self.rear = new_node
		circular_queue.q_len += 1
		print('Element {} inserted in queue.'.format(val))

	def dequeue(self):
		if self.isEmpty():
			print('Queue is empty.')
		else:
			tmp = self.front
			if self.front == self.rear:			
				self.front, self.rear = None, None
			else:
				self.front = self.front.next_node
			circular_queue.q_len -= 1
			print('One element with value {} removed from front.'.format(tmp.val))	