class SinglyLinkedList():
    def __init__(self,value):
        #ste the vale to the Node
        self.value = value
        #set the next Node
        self.next_Node = None


#Basic Idea is I/P A - > B -> C -> D then O/P is A <- B <- C <- D
def linkedListReversal(head):
    currentNode = head
    nextNode = None
    previous = None

    while currentNode:
        nextNode = currentNode.next_Node
        currentNode.next_Node = previous
        previous = currentNode
        currentNode = nextNode
    return previous

boston = SinglyLinkedList('bos')
sanFrancisco = SinglyLinkedList('SF')
oakland = SinglyLinkedList('ok')

print(boston.value)
print(sanFrancisco.value)
print(oakland.value)

boston.next_Node = sanFrancisco
sanFrancisco.next_Node = oakland
print(boston.next_Node)
print(sanFrancisco.next_Node)
print(boston.next_Node.value)
print(sanFrancisco.next_Node.value)

print(linkedListReversal(boston))
print(sanFrancisco.next_Node.value)
print(oakland.next_Node.value)
