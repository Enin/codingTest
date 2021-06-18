# Given the root node of a directed graph,
# clone this graph by creating its deep copy so that
# the cloned graph has the same vertices and edges as the original graph.
#
# Let’s look at the below graphs as an example.
# If the input graph is G=(V,E) where V is set of vertices and E is set of edges,
# then the output graph (cloned graph) G’ = (V’, E’) such that V = V’ and E = E’.
# We are assuming that all vertices are reachable from the root vertex, i.e. we have a connected graph.
import collections
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

# class Graph:
#     def __init__(self, root):
#         self.root = root
#
#     def insert(self, value, neighbors):
#         self.current_node = Node(value)

def cloning_rec(root, nodes_completed):
    if not root:
        return None

    pNew = Node(root.data)          # 루트 데이터 값을 갖는 헤드를 생성
    nodes_completed[root] = pNew    # 빈 입력을 받고 pNew 노드를 root번째 값에 입력할 것.

    for p in root.neighbors:        # 인접 노드 정보를 이터레이트
        x = nodes_completed.get(p)  # 노드
        if not x:
            pNew.neighbors += [cloning_rec(p, nodes_completed)]
        else:
            pNew.neighbors += [x]
    return pNew

def clone(root):
    nodes_completed = {}
    return cloning_rec(root, nodes_completed)


# un-directed gragh는 상호 노드가 서로 연결되어 있으며 자기 자신과는 연결되지 않는 노드이다.
# 최대 (nodes * nodes - nodes) / 2 의 edge가 존재한다.
def create_test_graph_undirected(nodes_count, edges_count):
    vertices = []
    for i in range(nodes_count):
        vertices += [Node(i)]   # vertices에 노드를 생성

    all_edges = []
    for i in range(edges_count):
        for j in range(i+1, nodes_count):
            all_edges.append([i, j])    # i와 j 사이의 연결을 추가한다.
                                        # 이때 본인과는 연결되지 않으므로 i+1부터 시작하고 이전 노드는 연결이 되어있으므로 추가 안해도됨.
    # 가능한 모든 연결을 생성한 뒤 랜덤하게 셔플한다.
    random.shuffle(all_edges)   # 에지의 순서를 섞는다
    print('all edges:', all_edges)

    for i in range(min(edges_count, len(all_edges))):   # 에지의 숫자와 모든 에지 조건중 적은 수만큼 에지로 사용한다.
        edge = all_edges[i]
        print('edge:', edge)
        vertices[edge[0]].neighbors += [vertices[edge[1]]]  # 생성한 vertices의 0번에지의 인접자에 1번에지를 추가
        vertices[edge[1]].neighbors += [vertices[edge[0]]]  # 반대로 마찬가지
        # edge[0]번 노드의 neighbors 리스트에 edge[1] 값을 리스트 add 로 합성하여준다. 반대로도 마찬가지

    return vertices

def print_graph_ver(vertices):
    for n in vertices:
        print(str(n.data), end = ': { ')
        for t in n.neighbors:
            print(str(t.data), end=' ')
        print('}')

def print_graph_rec(root, visited_nodes):
    if not root or root in visited_nodes:
        return

    visited_nodes.add(root)

    print(str(root.data), end=': { ')
    for n in root.neighbors:
        print(str(n.data), end=' ')
    print('}')

    for n in root.neighbors:
        print_graph_rec(n, visited_nodes)

def print_graph(root):
    visited_nodes = set()
    print_graph_rec(root, visited_nodes)

if __name__ == '__main__':
    vertices = create_test_graph_undirected(7, 18)
    print("generate graph:")
    print_graph_ver(vertices)
    print('....')
    print_graph(vertices[0])
    cp = clone(vertices[0])
    print()
    print('copied:')
    print(cp)
    print_graph(cp)