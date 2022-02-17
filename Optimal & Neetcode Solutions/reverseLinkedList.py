from lib2to3.pytree import Node
from re import I
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class IterativeSolution:
    def reverseList(self, head):
        # OPTIMAL SOLUTION
        # time: O(n) memory: O(1)

        # 'None' node will end up being the null at the end of LL
        previous, current = None, head

        while current:
            # swap pointer
            tempNode = current.next
            current.next = previous

            # increment nodes
            previous = current
            current = tempNode

        return previous


class RecursiveSolution:
    def reverseList(self, head):

        # time: O(n) memory: O(n)

        if not head:
            return None

        # head is current node in recursive call
        newHead = head

        # reverse link between next node and head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        # if head is the first node (i.e. becoming the last), set the pointer to null
        head.next = None
        return newHead


linkedList = ListNode(1, ListNode(5, ListNode(9, ListNode(11))))
iterative = IterativeSolution()
recursive = RecursiveSolution()

iterativeNewHead = iterative.reverseList(linkedList)
recursiveNewHead = recursive.reverseList(linkedList)
