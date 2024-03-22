class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def add_two_numbers(l1, l2):
    dummy_head = Node(0)
    current = dummy_head
    carry = 0

    p1, p2 = l1.head, l2.head

    while p1 or p2 or carry:
        value = carry
        if p1:
            value += p1.value
            p1 = p1.next
        if p2:
            value += p2.value
            p2 = p2.next

        carry = value // 10
        value %= 10

        current.next = Node(value)
        current = current.next

    return dummy_head.next

def input_linked_list():
    linked_list = LinkedList()
    values = input("Nhập các giá trị của danh sách liên kết (cách nhau bằng dấu cách): ").split()
    for value in values:
        linked_list.append(int(value))
    return linked_list

print("Nhập danh sách liên kết thứ nhất:")
num1 = input_linked_list()

print("Nhập danh sách liên kết thứ hai:")
num2 = input_linked_list()

sum_list = add_two_numbers(num1, num2)

result = []
current = sum_list
while current:
    result.append(str(current.value))
    current = current.next

print("Danh sách tổng:", " -> ".join(result[::-1]))
