class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome_linked_list(head):
    if not head or not head.next:
        return True

    # Tìm giá trị của nút giữa
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Đảo ngược phần phía sau của danh sách liên kết
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # So sánh giá trị của phần phía trước và phía sau của danh sách liên kết
    while prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next

    return True

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

if is_palindrome_linked_list(head):
    print("Danh sách liên kết là một palindrome.")
else:
    print("Danh sách liên kết không phải là một palindrome.")
