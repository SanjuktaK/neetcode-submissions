"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp = head

        #copying

        while temp:
            copynode = Node(temp.val)
            copynode.next = temp.next
            temp.next = copynode
            temp = temp.next.next

        # random

        temp = head

        while temp:
            copynode = temp.next
            copynode.random = temp.random.next if temp.random else None
            temp = temp.next.next
        
        # step 3: copying the next
        dummy = Node(-1)
        res = dummy
        temp = head
        while temp:
            res.next = temp.next
            res = res.next
            temp.next = temp.next.next
            temp = temp.next
        return dummy.next
            

        