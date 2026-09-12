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
        curr = head
        mpp ={}

        while curr:
            newNode = Node(curr.val)
            mpp[curr] = newNode
            curr = curr.next
        
        curr = head

        while curr:
            copyNode = mpp[curr]
            copyNode.next = mpp.get(curr.next)
            copyNode.random = mpp.get(curr.random)
            curr = curr.next
        return mpp[head]

        