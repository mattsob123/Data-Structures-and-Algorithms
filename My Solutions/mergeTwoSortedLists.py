class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        newHead = None
        point1, point2 = list1, list2

        if point1 == None and point2 == None:
            return None
        elif point1 == None:
            return list2
        elif point2 == None:
            return list1

        if point1.val > point2.val:
            newHead = point2
            point2 = point2.next
        else:
            newHead = point1
            point1 = point1.next

        newListPointer = newHead

        while point1 and point2:
            if point1.val > point2.val:
                newListPointer.next = point2
                point2 = point2.next
            else:
                newListPointer.next = point1
                point1 = point1.next

            newListPointer = newListPointer.next

        if point1:
            while point1:
                newListPointer.next = point1
                newListPointer = newListPointer.next
                point1 = point1.next
        if point2:
            while point2:
                newListPointer.next = point2
                newListPointer = newListPointer.next
                point2 = point2.next

        return newHead


linkedList = ListNode(1, ListNode(5, ListNode(9, ListNode(11))))
linkedList1 = ListNode(1, ListNode(5, ListNode(9, ListNode(11))))

mergeLists = Solution()
print(mergeLists.mergeTwoLists(linkedList, linkedList1))
