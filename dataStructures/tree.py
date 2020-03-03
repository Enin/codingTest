# 트리 설계 노드. 좌, 우측 노드 정보를 저장해야함.
from operator import le


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # 좌측 노드 정보
        self.right = None  # 우측 노드 정보

    # 노드가 가지는 사이즈와 뎁스 정보.
    def size(self):
        L = self.left.size() if self.left else 0  # 왼쪽의 사이즈 메서드를 재귀. 없을 경우 0
        R = self.right.size() if self.right else 0  # 위와 같다.
        return L + R + 1  # 왼쪽과 오른쪽의 크기 + 루트크기

    def depth(self):
        left_depth = self.left.depth() if self.left else 0  # size와 유사하게 메서드 재귀로 크기 받아옴.
        right_depth = self.right.depth() if self.right else 0  # 위와 같다.
        return left_depth + 1 if left_depth > right_depth else right_depth + 1  # 왼쪽과 오른쪽중 큰 뎁스를 리턴.

    # 순회연산 구현.
    def pre_order(self):
        traverse = list()
        traverse.append(self.data)  # 루트 먼저 받아옴.
        if self.left:
            traverse += self.left.pre_order()  # 왼쪽 자식노드로 이동 후 메서드 재귀.
        if self.right:
            traverse += self.right.pre_order()  # 오른쪽 자식노드로 이동.
        return traverse

    def in_order(self):
        traverse = list()
        if self.left:
            traverse += self.left.in_order()  # 왼쪽 자식노드로 이동하여 순회연산 수행
        traverse.append(self.data)  # 루트 받아옴.
        if self.right:
            traverse += self.right.in_order()
        return traverse

    def post_order(self):
        traverse = list()
        if self.left:
            traverse += self.left.post_order()  # 왼쪽 자식노드로 이동하여 순회연산 수행
        if self.right:
            traverse += self.right.post_order()
        traverse.append(self.data)  # 루트 받아옴.
        return traverse


class BinaryTree:
    def __init__(self, root):
        self.root = root  # 최초 노드 생성시 루트 노드를 생성.

    def size(self):
        if self.root:
            return self.root.size()  # 루트 노드일때 루트 노드의 사이즈 메서드 호출.
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def in_order(self):
        if self.root:
            return self.root.in_order()
        else:
            return []

    def pre_order(self):
        if self.root:
            return self.root.pre_order()
        else:
            return []

    def post_order(self):
        if self.root:
            return self.root.post_order()
        else:
            return []


# anytree 사용.
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

root_node = Node("root", data=10)
s1 = Node("s1", parent=root_node, data=5)
s2 = Node("s2", parent=root_node, data=6)

print(s1.data)

for pre, fill, node in RenderTree(root_node):
    print("%s%s %s" % (pre, node.name, node.data))
