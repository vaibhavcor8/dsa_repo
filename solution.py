# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Agar list khali hai ya sirf 1 node hai, toh swap ki zaroorat nahi
        if not head or not head.next:
            return head
        
        # Dummy node banate hain jo head se pehle rahega
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Jab tak aage kam se kam 2 nodes hain, tab tak loop chalega
        while current.next and current.next.next:
            # Nodes ko identify karein
            first = current.next
            second = current.next.next
            
            # Swapping ka asli logic yahan hai
            first.next = second.next
            second.next = first
            current.next = second
            
            # Agle pair par jaane ke liye 'current' ko 2 step aage badhayein
            current = first
            
        return dummy.next