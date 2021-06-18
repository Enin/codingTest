###
# Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
# Consider two sorted linked lists and the merged list below them as an example.
import random

def merge_sorted(head1, head2):
    merge_list = []
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    if head1[-1] <= head2[0]:
        head1.extend(head2)
        return head1
    elif head2[-1] <= head1[0]:
        head2.extend(head1)
        return head2

    while head1 and head2:
        if head1[0] <= head2[0]:
            temp = head1.pop(0)
            merge_list.append(temp)

        elif head1[0] > head2[0]:
            temp = head2.pop(0)
            merge_list.append(temp)

    if head1:
        merge_list.extend(head1)
    elif head2:
        merge_list.extend(head2)

    return merge_list

def test(n,m):
    list1 = random.sample(range(1,n),m)
    list2 = random.sample(range(1,n),m)
    list1.sort()
    list2.sort()
    print("list1 is {}, list2 is {}.".format(list1, list2))
    list3 = merge_sorted(list1, list2)

    print("merged list is {}".format(list3))

def main():
    test(20,4)
main()