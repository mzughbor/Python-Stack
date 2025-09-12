class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    def __repr__(self):
        return f"ListNode({self.val!r})"

class CustomNode(object):
    def __init__(self,val,*bonus):
        self.val = val
        self.next = None
        self.bonus = bonus
    def __repr__(self):
        return f"CustomNode({self.val!r}, bonus={self.bonus!r})"


class LinkedList(object):
    def __init__(self):
        self.head = None
    def addNode(self, val, *extras):
        if not self.head:
            if extras:
                self.head = CustomNode(val, extras)
            else:
                self.head = ListNode(val)
            return self
        current = self.head
        while current.next:
            current = current.next
        if extras:
            current.next = CustomNode(val,extras)
        else:
            current.next = ListNode(val)
        return self
    def __repr__(self):
        nodes = []
        cur = self.head
        while cur:
            # use the node's repr for concise display
            nodes.append(repr(cur))
            cur = cur.next
        return " -> ".join(nodes)



myList = LinkedList()
myList.addNode(72,"hello world", "banana").addNode(45).addNode(21, "Yay")

print(myList)
print(myList.head)
print(myList.head.next)
print(myList.head.next.next.bonus)


