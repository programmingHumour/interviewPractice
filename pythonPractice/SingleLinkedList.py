#Create a Node
#Point Each node to an element in it and the next node
class SinglyLinkedList():
    def __init__(self,value):
        #ste the vale to the Node
        self.value = value
        #set the next Node
        self.next_Node = None

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
