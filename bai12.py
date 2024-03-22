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

    def delete_node(self, index):
        if index < 0:
            print("Chỉ mục không hợp lệ.")
            return None
        elif index == 0:
            if self.head:
                deleted_node = self.head
                self.head = self.head.next
                deleted_node.next = None
                return deleted_node
            else:
                print("Danh sách liên kết đã rỗng.")
                return None
        else:
            prev_node = None
            temp_node = self.head
            current_index = 0
            while temp_node and current_index != index:
                prev_node = temp_node
                temp_node = temp_node.next
                current_index += 1
            
            if temp_node:
                deleted_node = temp_node
                prev_node.next = temp_node.next
                deleted_node.next = None
                return deleted_node
            else:
                print("Chỉ mục vượt quá kích thước của danh sách liên kết.")
                return None

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value) + ' -> '
            temp_node = temp_node.next
        return result + 'None'

# Hàm chính
if __name__ == "__main__":
    linked_list = LinkedList()
    
    # Nhập từ bàn phím và chèn vào cuối danh sách liên kết
    while True:
        value = input("Nhập giá trị mới (nhập 'q' để kết thúc): ")
        if value == 'q':
            break
        linked_list.append(int(value))
    
    # In ra danh sách liên kết trước khi xóa
    print("Danh sách liên kết trước khi xóa:")
    print(linked_list)

    # Nhập chỉ mục của nút cần xóa
    index = int(input("Nhập chỉ mục của nút cần xóa: "))

    # Xóa nút từ danh sách liên kết
    deleted_node = linked_list.delete_node(index)

    # In ra nút đã xóa
    if deleted_node:
        print("Nút đã xóa:", deleted_node.value)
    else:
        print("Không thể xóa nút.")

    # In ra danh sách liên kết sau khi xóa
    print("Danh sách liên kết sau khi xóa:")
    print(linked_list)
