# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        res_head = None
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                if res is None:
                    res = ListNode(list1.val)
                    res_head = res
                else:
                    res.next = ListNode(list1.val)
                    res = res.next
                list1 = list1.next
            else:
                if res is None:
                    res = ListNode(list2.val)
                    res_head = res
                else:
                    res.next = ListNode(list2.val)
                    res = res.next
                list2 = list2.next
        
        if res is not None:
            if list1 is not None:
                res.next = list1
            else:
                res.next = list2
        else:
            if list1 is not None:
                res = list1
                res_head = res
            else:
                res = list2
                res_head = res

        return res_head