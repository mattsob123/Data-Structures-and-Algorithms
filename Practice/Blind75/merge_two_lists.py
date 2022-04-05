class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if not list1: return list2
    if not list2: return list1
    
    l1, l2 = list1, list2
    
    merge_list = ListNode(0)
    curr = merge_list
    
    while list1 and list2:
        if list1.val > list2.val:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        else:
            curr.next = list1
            curr = curr.next
            list1 = list1.next
            
    if list1:
        curr.next = list1
    else:
        curr.next = list2
        
    return merge_list.next