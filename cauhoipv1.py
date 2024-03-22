class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    if not head:
        return None
    seen_values = set()
    seen_values.add(head.value)
    current_node = head

    while current_node.next:
        if current_node.next.value in seen_values:
            current_node.next = current_node.next.next
        else:
            seen_values.add(current_node.next.value)
            current_node = current_node.next
    return head
def print_list(head):
    result = []
    current_node = head
    while current_node:
        result.append(current_node.value)
        current_node = current_node.next
    print(result)

def input_linked_list():
    head = None
    tail = None
    while True:
        value = input("Nhập giá trị (nhấn Enter để kết thúc nhập): ")
        if value == "":
            break
        new_node = ListNode(int(value))
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

print("Nhập danh sách liên kết:")
head = input_linked_list()

print("Danh sách gốc:")
print_list(head)

new_head = remove_duplicates(head)

print("Danh sách sau khi loại bỏ các phần tử trùng lặp:")
print_list(new_head)
