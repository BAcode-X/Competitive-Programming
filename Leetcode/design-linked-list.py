class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1
        ind = 0
        cur = self.head
        while ind < index:
            cur = cur.next
            ind += 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.len:
            return
        new = Node(val)
        cur = self.head
        if index <= 0:
            new.next = cur
            self.head = new
        else:
            ind = 0
            while ind < index-1:
                cur = cur.next
                ind += 1
            new.next = cur.next
            cur.next = new
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return
        cur = self.head
        if index == 0:
            self.head = self.head.next
        else:
            ind = 0
            while ind < index-1:
                cur = cur.next
                ind += 1
            cur.next = cur.next.next
        self.len -= 1
