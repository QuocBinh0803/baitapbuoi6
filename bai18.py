class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    prev, current = dummy, head
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    return dummy.next
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
val = int(input("Nhập giá trị cần loại bỏ từ danh sách liên kết: "))
print("Danh sách liên kết gốc:")
print_linked_list(head)
new_head = remove_elements(head, val)
print("Danh sách liên kết sau khi loại bỏ các nút có giá trị", val, ":")
print_linked_list(new_head)
