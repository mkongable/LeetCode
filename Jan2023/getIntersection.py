class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    # traverse all nodes in headA and store them in a set
    # traverse all nodes in headB and return the first node that is in the set
    # if no node is in the set, return None

    discovered = set()
    while headA:
        discovered.add(headA)
        headA = headA.next
    
    while headB:
        if headB in discovered:
            return headB
        headB = headB.next

    return None

# create a sample linked list
head = ListNode(1)
print(head.val)
head.next = ListNode(2)
head.next.next = ListNode(3)
head2 = ListNode(4)
head2.next = head.next.next

# test the function
print(getIntersectionNode(head, head2).val)
print(head.val)