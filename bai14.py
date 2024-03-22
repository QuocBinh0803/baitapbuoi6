class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def tim_nut_giua(head):
    if not head:
        return None   
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
def nhap_danh_sach():
    nhap = input("Nhập các giá trị của danh sách liên kết, cách nhau bằng khoảng trắng: ").split()
    if not nhap:
        return None
    head = Node(int(nhap[0]))
    current = head
    for item in nhap[1:]:
        current.next = Node(int(item))
        current = current.next
    return head
danh_sach = nhap_danh_sach()
print("Danh sách liên kết:")
current = danh_sach
while current is not None:
    print(current.value, end=" ")
    current = current.next
middle_node = tim_nut_giua(danh_sach)
if middle_node:
    print("\nNút giữa của danh sách liên kết là:", middle_node.value)
else:
    print("\nDanh sách liên kết rỗng.")
