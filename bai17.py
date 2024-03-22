class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def delete_duplicates(head):
    if not head or not head.next:
        return head
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()
# Nhập danh sách liên kết từ người dùng
def input_linked_list():
    input_values = input("Nhập các giá trị cho danh sách liên kết (cách nhau bằng dấu cách): ").split()
    if not input_values:
        return None
    head = ListNode(int(input_values[0]))
    current = head
    for value in input_values[1:]:
        current.next = ListNode(int(value))
        current = current.next
    return head
# Nhập danh sách liên kết từ người dùng
head = input_linked_list()
print("Danh sách liên kết gốc:")
print_linked_list(head)
# Loại bỏ các phần tử trùng lặp
new_head = delete_duplicates(head)
print("Danh sách liên kết sau khi loại bỏ các phần tử trùng lặp:")
print_linked_list(new_head)
