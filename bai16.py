class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    return dummy.next
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()
# Nhập danh sách liên kết thứ nhất từ người dùng
def input_linked_list_1():
    input_values = input("Nhập các giá trị cho danh sách liên kết thứ nhất (cách nhau bằng dấu cách): ").split()
    if not input_values:
        return None
    head = ListNode(int(input_values[0]))
    current = head
    for value in input_values[1:]:
        current.next = ListNode(int(value))
        current = current.next
    return head
# Nhập danh sách liên kết thứ hai từ người dùng
def input_linked_list_2():
    input_values = input("Nhập các giá trị cho danh sách liên kết thứ hai (cách nhau bằng dấu cách): ").split()
    if not input_values:
        return None
    head = ListNode(int(input_values[0]))
    current = head
    for value in input_values[1:]:
        current.next = ListNode(int(value))
        current = current.next
    return head
# Nhập danh sách liên kết thứ nhất và thứ hai từ người dùng
list1 = input_linked_list_1()
list2 = input_linked_list_2()
print("Danh sách liên kết thứ nhất:")
print_linked_list(list1)
print("Danh sách liên kết thứ hai:")
print_linked_list(list2)
# Hợp nhất hai danh sách liên kết và in kết quả
merged_list = merge_two_lists(list1, list2)
print("Danh sách liên kết sau khi hợp nhất:")
print_linked_list(merged_list)
