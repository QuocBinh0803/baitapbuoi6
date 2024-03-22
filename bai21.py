class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

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

middle_node = middle_of_linked_list(head)
print("Node giữa của danh sách liên kết là:", middle_node.val)
