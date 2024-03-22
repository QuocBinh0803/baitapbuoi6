class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_duplicates(linked_list):
    if not linked_list:
        return linked_list
    
    current = linked_list
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return linked_list

def print_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Nhập danh sách liên kết từ người dùng
def input_linked_list():
    input_values = input("Nhập các giá trị cho danh sách liên kết (cách nhau bằng dấu cách): ").split()
    if not input_values:
        return None
    head = Node(int(input_values[0]))
    current = head
    for value in input_values[1:]:
        current.next = Node(int(value))
        current = current.next
    return head

# Nhập danh sách liên kết từ người dùng
original_list = input_linked_list()

print("Danh sách liên kết gốc:")
print_linked_list(original_list)

# Loại bỏ các phần tử trùng lặp
new_list = remove_duplicates(original_list)

print("Danh sách liên kết sau khi loại bỏ các phần tử trùng lặp:")
print_linked_list(new_list)
