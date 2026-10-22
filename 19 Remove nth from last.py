class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None: # type: ignore
        dummy = ListNode(0, head) # type: ignore
        first = dummy
        second = dummy

        # Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next