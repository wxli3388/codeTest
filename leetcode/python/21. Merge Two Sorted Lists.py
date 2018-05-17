# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        
        temp = ListNode(0)
        head = temp
        
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next

        if l1==None and l2!=None:
            temp.next=l2
        elif l1!=None and l2==None:
            temp.next=l1
            
        return head.next