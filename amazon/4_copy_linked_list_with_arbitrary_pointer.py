###
# You are given a linked list where the node has two pointers.
# The first is the regular next pointer.
# The second pointer is called arbitrary_pointer and it can point to any node in the linked list.
# Your job is to write code to make a deep copy of the given linked list.
# Here, deep copy means that any operations on the original list should not affect the copied list.
# 아비터리 포인터를 사용하는 링크드 리스트
# 주어진 링크드 리스트에 대한 딮카피를 수행할 것.
import random
import copy


def deep_copy_arbitrary_pointer(head):
    if not head:
        return None
    
    arbit_head = copy.deepcopy(head)
