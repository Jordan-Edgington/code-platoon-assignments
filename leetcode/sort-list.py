# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return self.__str__()


"""
Given the head of a linked list, return the list after sorting it in ascending order

[4, 2, 1, 3]

Determine midpoint (use helper func)



"""


class Solution:
    def __init__(self):
        pass

    def sortList(self, head):
        if not head or not head.next:
            return head
        # midpoint
        mid_point = self.MidPoint(head)
        # left/right recursive
        left = self.sortList(head)
        right = self.sortList(mid_point)
        # merge
        return self.Merge(left, right)

    def MidPoint(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def Merge(self, left, right):
        dummy = curr = ListNode(0)  # same link ref
        # curr = ListNode(0) # diff link ref
        while left and right:
            if left.val < right.val:  # 4, 2
                curr.next = left
                curr = curr.next
                left = left.next
            else:
                curr.next = right
                curr = curr.next
                right = right.next
        curr.next = left or right
        return dummy.next


test4 = ListNode(3)
test3 = ListNode(1, test4)
test2 = ListNode(2, test3)
test1 = ListNode(4, test2)
print(f"{test1} {test1.next} {test1.next.next} {test1.next.next.next} {test1.next.next.next.next}")
answer = Solution()
print(answer.sortList(test1))
print(test1)
print(test1.next)
# print(test1.next.next)

print(f"{test3} {test3.next} {test3.next.next} {test3.next.next.next} {test3.next.next.next.next}")
