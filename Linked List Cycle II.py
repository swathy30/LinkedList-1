class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        slow = head
        fast = head
        cycle = False
        
        while fast!= None and fast.next!= None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                cycle = True
                break
        if cycle!= True:
            return None
        
        slow = head
        
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow
    