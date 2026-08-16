class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at a specific position (0-based index)
    def insert_position(self, pos, data):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete from beginning
    def delete_begin(self):
        if self.head is None:
            print("List is Empty")
            return

        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Search an element
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    # Display the linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next

        print("None")


# Driver Code
ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(40)

ll.insert_position(2, 30)

ll.insert_begin(5)

ll.display()

print(ll.search(30))

ll.delete_begin()
ll.display()

ll.delete_end()
ll.display()