class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        cur = self.head
        i = 0
        while cur and i < index - 1:
            cur = cur.next
            i += 1

        if cur is None:
            return  # index is greater than length, do nothing

        newNode = Node(val)
        newNode.next = cur.next
        cur.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        cur = self.head
        i = 0
        while cur and i < index - 1:
            cur = cur.next
            i += 1

        if cur is None or cur.next is None:
            return

        cur.next = cur.next.next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        newList = []
        revList = [] 
        
        while head:
            newList.append(head.val)
            head = head.next
        
        for n in newList[:]:
            revList.append(newList[-1])
            newList.pop()

        #THIS ONE RIGHT HERE
        head = ListNode(revList[0])
        
        current = head

        for n in revList[1:]:
            current.next = ListNode(n)
            current = current.next

        return head
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newList = []
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val < l2.val:
                newList.append(l1.val)
                l1 = l1.next
            elif l1.val > l2.val or l1.val == l2.val:
                newList.append(l2.val)
                l2 = l2.next

        if l1 is None:
            while l2:
                newList.append(l2.val)
                l2 = l2.next
            
        elif l2 is None:
            while l1:
                newList.append(l1.val)
                l1 = l1.next
        
        dummy = ListNode(-1)
        current = dummy

        for n in newList:
            current.next = ListNode(n)
            current = current.next

        return dummy.next
