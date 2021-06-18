###
# Given the root of a binary tree, display the node values at each level.
# Node values for all levels should be displayed on separate lines.
# Let’s take a look at the below binary tree.
import collections # queue 라이브러리

class node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class binary_tree:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = node(value)
                    break


def create_BST(input):
    for i in range(len(input)):
        if i == 0:
            root = node(input[i])
            tree = binary_tree(root)
        else:
            tree.insert(input[i])

    return tree


def level_order_traversal(tree):
    queue = [collections.deque(), collections.deque()]
    current_queue = queue[0]
    next_queue = queue[1]

    current_queue.append(tree.head)
    tree_level = 0

    while current_queue:
        temp = current_queue.popleft()
        print(str(temp.value), end=" ")

        if temp.left is not None:
            next_queue.append(temp.left)

        if temp.right is not None:
            next_queue.append(temp.right)

        if not current_queue:
            print()
            tree_level += 1
            current_queue = queue[tree_level % 2]       # 다음 큐가 현재 큐로 변경되며
            next_queue = queue[(tree_level + 1) % 2]    # 비어있는 큐 queue[0]를 다음 큐로 사용

    print()

def main():
    arr = [100, 50, 200, 25, 75, 350]
    test_tree = create_BST(arr)
    print("level order traversal:")
    level_order_traversal(test_tree)

main()