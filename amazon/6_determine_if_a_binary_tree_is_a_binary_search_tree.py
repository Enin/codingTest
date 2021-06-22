###
# Given a Binary Tree, figure out whether it’s a Binary Sort Tree.
# In a binary search tree, each node’s key value is smaller than the key value of all nodes in the right subtree,
# and is greater than the key values of all nodes in the left subtree.
# Below is an example of a binary tree that is a valid BST.
import collections
class node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class BST:
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

    def check_tree(self):
        self.queue = [collections.deque(), collections.deque()]
        self.current_queue = self.queue[0]
        self.next_queue = self.queue[1]
        self.tree_level = 0

        self.current_queue.append(self.head)
        while self.current_queue:
            self.temp = self.current_queue.popleft()
            if self.temp.left is not None:
                if self.temp.value < self.temp.left.value:
                    print("worng BST on level {}. {} < {}".format(self.tree_level, self.temp.value, self.temp.value.left.value))
                    return False
                self.next_queue.append(self.temp.left)

            if self.temp.right is not None:
                if self.temp.value > self.temp.right.value:
                    print("worng BST on level {}. {} > {}".format(self.tree_level, self.temp.value, self.temp.value.left.value))
                    return False
                self.next_queue.append(self.temp.right)

            if not self.current_queue:
                self.tree_level += 1
                self.current_queue = self.queue[(self.tree_level % 2)]
                self.next_queue = self.queue[(self.tree_level + 1) % 2]

        print("The tree is correct BST")
        return True


def create_BST(input):
    for i in range(len(input)):
        if i == 0:
            root = node(input[i])
            tree = BST(root)
        else:
            tree.insert(input[i])

    return tree



def main():
    arr = [100, 50, 200, 25, 75, 90, 350]
    test_tree = create_BST(arr)
    result = test_tree.check_tree()
    print(result)


main()