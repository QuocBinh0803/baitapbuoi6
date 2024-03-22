class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    def get_length_and_tail(node):
        length = 0
        tail = None
        while node:
            length += 1
            if not node.next:
                tail = node
            node = node.next
        return length, tail
    lengthA, tailA = get_length_and_tail(headA)
    lengthB, tailB = get_length_and_tail(headB)
    if tailA != tailB:
        return None
    diff = abs(lengthA - lengthB)
    longer_head = headA if lengthA > lengthB else headB
    shorter_head = headB if lengthA > lengthB else headA

    for _ in range(diff):
        longer_head = longer_head.next
    while longer_head and shorter_head:
        if longer_head == shorter_head:
            return longer_head
        longer_head = longer_head.next
        shorter_head = shorter_head.next
    return None
def input_linked_list():
    linked_list = None
    values = input("Nhập giá trị của danh sách liên kết (cách nhau bằng dấu cách): ").split()
    prev_node = None
    for value in values:
        node = ListNode(int(value))
        if prev_node:
            prev_node.next = node
        else:
            linked_list = node
        prev_node = node
    return linked_list

print("Nhập danh sách liên kết thứ nhất:")
headA = input_linked_list()

print("Nhập danh sách liên kết thứ hai:")
headB = input_linked_list()

intersection_node = get_intersection_node(headA, headB)

if intersection_node:
    print("Giá trị của nút giao nhau:", intersection_node.val)
else:
    print("Không tìm thấy nút giao nhau")
