class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l11, l22 = [], []
        
        current = l1
        while current:
            l11.append(current.val)
            current = current.next
            
        current = l2
        while current:
            l22.append(current.val)
            current = current.next
        

        result_l1 = int("".join(map(str, reversed(l11))))  
        result_l2 = int("".join(map(str, reversed(l22))))  
        result_sum = result_l1 + result_l2
        

        dummy = ListNode(0)
        current = dummy
        

        for digit_char in reversed(str(result_sum)):
            current.next = ListNode(int(digit_char))
            current = current.next
            
        return dummy.next
