class Node:
    
    def __init__(self, data, next_node = None): # Initializes a node object
        self.data = data
        self.next_node = next_node
        
class Linked_List:

    length = 0 # Used to store length of the list

    def __init__(self): # Initializes a linked list object - same object will remain throughout the code execution
        self.head = None
                
    def isEmpty(self): # Function to check if the list is empty 
        if self.head is None:
            return 1

    '''The index values used are at the discretion of the programmer - you can modify the code to use your value logic'''
    def insert(self, val, index = -1): # Function to insert the element in the list - default index is -1, which means add at the end
        if self.isEmpty():
            node = Node(val)
            self.head = node
            print('Value {} inserted.'.format(val))
        else:
            if (index <= -1) | (index > Linked_List.length): # In case a user gives index value less than -1 or greater than the list length,
                itr = self.head                              # the code will handle it by adding the element at the end - one of the ways
                while itr.next_node != None:                 # of handling invalid inputs
                    itr = itr.next_node
                node = Node(val)
                itr.next_node = node
                print('Value {} inserted at the end.'.format(val))
            elif index == 0: # Index = 0 will insert the element at the beginning of the list
                node = Node(val)
                node.next_node = self.head
                self.head = node
                print('Value {} inserted at the beginning.'.format(val))
            else:
                itr = self.head
                cnt = 0 # Used to reach to an element in the list
                while cnt < index-1:
                    itr = itr.next_node
                    cnt += 1
                node = Node(val)
                node.next_node = itr.next_node
                itr.next_node = node
                print('Value {} inserted at the index {}.'.format(val, index))        
        Linked_List.length += 1

    '''To remove a node, we use free() in C. However, in Python, we have a deafult garbage collector for unreferenced objects running
       at the backend.'''    
    def remove(self, index = -1): # Default index = -1 will remove the element from front of the list
        if self.isEmpty():
            print('Empty linked list.')
            return
        if (index < -1) | (index > Linked_List.length): # Another variation of invalid input handling - return without any operation
            print('Invalid index.')
            return
        if (index >= -1) & (index < 1): # If index is -1 or 0, remove node from the front - again, the default behavior can be modified
            tmp = self.head.data        # to instead remove an element from the end of the list
            self.head = self.head.next_node
            print('Value {} present at index {} removed from the linked list.'.format(tmp, index))
        else:
            itr = self.head # this iterator will move to node at index - 1
            itr2 = self.head.next_node # this iterator will move to node at index
            cnt = 0
            while cnt < index-1:
                itr = itr.next_node
                itr2 = itr2.next_node
                cnt += 1
            print('Value {} present at index {} removed from the linked list.'.format(itr2.data, index))
            itr2 = itr2.next_node
            itr.next_node = itr2
        Linked_List.length -= 1    

    def read_modify(self, index, val = None): # By default, the function will just read a value at a given index
        if self.isEmpty():
            print('Empty linked list.')
            return
        if (index > Linked_List.length) | (index < 0):
            print('Invalid index.')
            return
        itr = self.head
        cnt = 0
        while cnt < index:
            itr = itr.next_node
            cnt += 1
        if val is None:
            print('Value at index {} is {}.'.format(index, itr.data))
        else:
            itr.data = val
            print('Modified value at index {} is {}.'.format(index, itr.data))

    def reverse(self):
        curr = self.head
        nxt = None
        prev = None
        while curr:
            nxt = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nxt
        self.head = prev
        print('List reversed.')

    def traverse(self):
        if self.head is None:
            print('No linked list to print.')
        else:
            itr = self.head
            ll = ''
            while itr:
                ll += str(itr.data) + '-->'
                itr = itr.next_node
            print(ll)
                
ll = Linked_List()
ll.traverse()
ll.insert(15,-20)
ll.traverse()
ll.insert(5,-1)
ll.insert(60,999)
ll.traverse()
ll.insert(3,0)
ll.traverse()
ll.insert(100,3)
ll.insert(150,1)
ll.traverse()
ll.read_modify(100)
ll.read_modify(2)
ll.read_modify(2,200)
ll.traverse()
ll.remove()
ll.traverse()
ll.remove(-111)
ll.remove(-560)
ll.remove(0)
ll.traverse()
ll.remove()
ll.traverse()
ll.remove(2)
ll.traverse()
ll.insert(175,3)
ll.traverse()
ll.reverse()
ll.traverse()
ll.reverse()
ll.traverse()
