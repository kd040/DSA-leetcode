class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None: # type: ignore
        self.prev = None
        self.current = head
        while self.current:
            self.next_node = self.current.next
            self.current.next = self.prev
            self.prev = self.current
            self.current = self.next_node
        return self.prev