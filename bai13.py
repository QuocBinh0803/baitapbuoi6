class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def dao_nguoc_danh_sach(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print("Nhập các giá trị của danh sách liên kết (nhấn Enter sau mỗi giá trị):")
giatri = input()
while giatri:
    giatri = int(giatri)
    if not head:
        head = Node(giatri)
    else:
        current = head
        while current.next:
            current = current.next
        current.next = Node(giatri)
    giatri = input()
print("Danh sách liên kết ban đầu:")
current = head
while current is not None:
    print(current.value, end=" ")
    current = current.next
head = dao_nguoc_danh_sach(head)
print("\nDanh sách liên kết sau khi đảo ngược:")
current = head
while current is not None:
    print(current.value, end=" ")
    current = current.next
