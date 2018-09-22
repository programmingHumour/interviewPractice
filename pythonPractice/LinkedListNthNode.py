class SinglyLinkedList():
    def __init__(self,value):
        #ste the vale to the Node
        self.value = value
        #set the next Node
        self.next_Node = None

#create two pointers then set the pointer at a distance of n-1 blocks from pointer1
#Then move along the both pointers until the pointer2 reaches the tail
def nth_last_node(n,head):

    pointer1 = head
    pointer2 = head

    for i in range(n-1):
        #check if the pointer2 has the next node if not then throw an error
        if not pointer2.next_Node:
            raise LookupError('Next node null')
        pointer2 = pointer2.next_Node
    #keep travesring until the next node reaches the tail
    while pointer2.next_Node:
        pointer2 = pointer2.next_Node
        pointer1 = pointer1.next_Node
    return pointer1.value


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

print(nth_last_node(1,boston))
