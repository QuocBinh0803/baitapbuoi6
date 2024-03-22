class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
        temp_node.next = new_node
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
        if value == 'q':
            break
        linked_list.append(int(value))
    print("Danh sách liên kết sau khi chèn vào cuối:")
    print(linked_list)
