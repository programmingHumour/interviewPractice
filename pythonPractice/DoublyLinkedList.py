#Create a Node
#Point Each node to the preceeding node and the next node
class DoublyLinkedList():
    def __init__(self,value):
        #set the value
        self.value = value
        self.next_Node = None
        self.prev_Node = None

providence = DoublyLinkedList('pvd')
boston = DoublyLinkedList('bos')
sanFrancisco = DoublyLinkedList('SF')
oakland = DoublyLinkedList('ok')

print(boston.value)
print(sanFrancisco.value)
print(oakland.value)

boston.next_Node = sanFrancisco
boston.prev_Node = providence
print(boston.next_Node.value)
print(boston.prev_Node.value)
