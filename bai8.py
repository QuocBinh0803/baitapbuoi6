class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

def insert_at_beginning(linked_list, value):
    linked_list.prepend(value)

linked_list = LinkedList()
linked_list.append(20)
linked_list.append(30)

print("Nguyen Quoc Binh:")
linked_list.display()

insert_at_beginning(linked_list, 10)

print("Nguyen Quoc Binh:")
linked_list.display()
