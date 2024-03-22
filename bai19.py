class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

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

head = input_linked_list()

print("Danh sách liên kết gốc:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)

print("Danh sách liên kết sau khi đảo ngược:")
print_linked_list(reversed_head)
