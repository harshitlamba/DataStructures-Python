import queue

if __name__ == '__main__':
	valid = 0
	while(valid == 0):
		menu_select = input('\nMenu:\n1. Simple Queue\n2. Circular Queue\n3. Priority Queue\n4. Double Ended Queue\n5. Exit \
							 \nEnter the queue type: ')
		if '.' in menu_select:
			print('Enter a valid choice.')
		else:
			try:
				option_num = int(menu_select)
				if (option_num < 1) | (option_num > 5):
					print('Enter a valid choice.')
				else:
					if option_num == 5:
						valid = 1
					else:
						if option_num == 1:
							q = queue.simple_queue()
						elif option_num == 2:
							max_size_flag = 0
							while max_size_flag == 0:
								inp = input('Enter maximum queue size (a float will be rounded off to floor): ')
								try:
									q = queue.circular_queue(int(float(inp)))
									max_size_flag = 1
								except:
									print('Invalid number entered.')
						elif option_num == 3:
							print('priority')
						elif option_num == 4:
							print('double ended')
						
						switcher = {'1':'Peek','2':'Enqueue','3':'Dequeue','4':'Is Empty','5':'Print','6':'Exit'}
						flag = 0
						while flag == 0:
							operation_select = input('\n1. Peek\n2. Enqueue\n3. Dequeue\n4. Is Empty\n5. Print\n6. Exit \
													  \nEnter the operation: ')
							select = switcher.get(operation_select, None)
							if  select is None:
								print('Enter a valid option.')
							else:
								if select == 'Peek':
									q.peek()
								elif select == 'Enqueue':
									inp = input('\nEnter the value to enqueue: ')
									q.enqueue(inp)
								elif select == 'Dequeue':
									q.dequeue()
								elif select == 'Is Empty':
									if q.isEmpty() == 1:
										print('Queue is empty.')
									else:
							 			print('Queue is not empty.')
								elif select == 'Print':
									q.print()
								else:
							 		if select == 'Exit':
							 			flag = 1
			except:
				print('Enter a valid choice.')									

