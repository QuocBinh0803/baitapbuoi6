# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def prepend(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#     def __str__(self):
#         temp_node = self.head
#         result = ''
#         while temp_node is not None:
#             result += str(temp_node.value) + ' -> '
#             temp_node = temp_node.next
#         return result + 'None'
# if __name__ == "__main__":
#     linked_list = LinkedList()
#     linked_list.prepend(10)
#     linked_list.prepend(20)
#     linked_list.prepend(30)
#     print("Danh sách liên kết sau khi chèn vào đầu:")
#     print(linked_list)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value) + ' -> '
            temp_node = temp_node.next
        return result + 'None'

if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        value = input("Nhập giá trị mới (nhập 'q' để kết thúc): ")
        if value == 'Binh':
            break
        linked_list.prepend(int(value))

    print("Danh sách liên kết sau khi chèn vào đầu:")
    print(linked_list)
