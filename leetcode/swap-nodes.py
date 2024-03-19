# ------------------------------------
# NOTE: This is unsolved.
# ------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}"


class Solution:
    def swapNodes(self, head, k):
        curr = head
        prev = None
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        curr = head
        search = 0
        found = False
        while curr:
            if search == k:
                search1 = search
                first_prev = prev
                first = curr
                first_next = curr.next
            elif search == ((length+1) - k):
                search2 = search
                second_prev = prev
                second = curr
                second_next = curr.next
                found = True
            if found == True and search2-search1 == 1:
                first_prev.next = second
                second.next = first
                first.next = second_next
                return second
            elif found == True and search == 2:
                second.next = first
                first.next = None
                return second
            elif found == True:
                first_prev.next = second
                second.next = first_next
                second_prev.next = first
                first.next = second_next
                return head
            search += 1
            prev = curr
            if search == length:
                pass
            else:
                curr = curr.next


answer = Solution()
test10 = ListNode(5)
test9 = ListNode(9, test10)
test8 = ListNode(0, test9)
test7 = ListNode(3, test8)
test6 = ListNode(8, test7)
test5 = ListNode(7, test6)
test4 = ListNode(6, test5)
test3 = ListNode(6, test4)
test2 = ListNode(2,)
test1 = ListNode(1, test2)
[7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
print(answer.swapNodes(test1, 1))
# print(test1)
# print(test1.next)
# print(test1.next.next)
# print(test1.next.next.next)
# print(test1.next.next.next.next)
# print(test1.next.next.next.next.next)
# print(test1.next.next.next.next.next.next)
# print(test1.next.next.next.next.next.next.next)
# print(test1.next.next.next.next.next.next.next.next)
# print(test1.next.next.next.next.next.next.next.next.next)
