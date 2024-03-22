class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value) + ' -> '
            temp_node = temp_node.next
        return result + 'None'

# Hàm chính
if __name__ == "__main__":
    n = int(input("Nhập số lượng node bạn muốn thêm vào danh sách liên kết: "))
    linked_list = None
    for i in range(n):
        value = int(input(f"Nhập giá trị của node {i + 1}: "))
        if not linked_list:
            linked_list = LinkedList(value)
        else:
            linked_list.append(value)

    print("Danh sách liên kết đã tạo:")
    print(linked_list)
