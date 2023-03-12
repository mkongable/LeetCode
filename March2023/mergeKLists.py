def mergeKLists(self,lists:List[Optional[ListNode]])->Optional[ListNode]:
    values,head,pointer=[],None,None
    for l in lists:
        while l:
            heappush(values,l.val)
            l=l.next

    while values:
        if head is None:
            head=ListNode(heappop(values))
            pointer=head

        else:
            pointer.next=ListNode(heappop(values))
            pointer=pointer.next

    return head