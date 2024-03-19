#!/usr/bin/env python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}"
# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.


class Solution:
    def __init__(self):
        pass

    def removeNodes(self, head):
        new_head = self.reverseNodes(head)
        current_high = new_head.val

        curr = new_head.next
        prev = new_head
        while curr is not None:
            if curr.val > current_high:
                current_high = curr.val
                prev = curr
                curr = curr.next
            elif curr.val < current_high:
                self.deleteNode(prev)
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return self.reverseNodes(new_head)

    def reverseNodes(self, head):
        prev = None
        curr = head
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

    def deleteNode(self, prev):
        if prev.next.next is not None:
            prev.next = prev.next.next
        else:
            prev.next = None


answer = Solution()
test6 = ListNode(5)
test5 = ListNode(6, test6)
test4 = ListNode(3, test5)
test3 = ListNode(4, test4)
test2 = ListNode(8, test3)
test1 = ListNode(2, test2)

print(answer.removeNodes(test1))
print(f"{test2} {test2.next} {test2.next.next}")
