class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# 10 -> 20 -> 30 -> Noneという連結リスト
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
# node3.next は None のまま（終点）

head = node1

# トラバーサル（走査）
# 先頭さえわかれば、矢印をたどってアクセスできる
def print_list(head):
    current = head

    while current:
        print(f"[{current.val}]", end=" -> ")
        current = current.next

    print("None")

# 練習問題
# 10と20の間に15を入れる
node_new = Node(15)
node_new.next = node2
node1.next = node_new

print_list(head)

