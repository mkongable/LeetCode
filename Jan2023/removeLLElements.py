class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    # traverse the linked list, to remove all nodes with value val
    # return the new head of the linked list
    # if the head is removed, return the new head
    # if the linked list is empty, return None

    # create a dummy node
    dummy = ListNode(0)
    dummy.next = head

    # traverse the linked list
    prev = dummy
    while prev.next:
        if prev.next.val == val:
            prev.next = prev.next.next
        else:
            prev = prev.next

    return dummy.next