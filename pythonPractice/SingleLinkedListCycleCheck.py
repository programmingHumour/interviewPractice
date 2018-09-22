class SinglyLinkedList():
    def __init__(self,value):
        #ste the vale to the Node
        self.value = value
        #set the next Node
        self.next_Node = None

#Basic anaolgy behind this consider two tracks one circular and one straigt with two runner one fast and one slow
#if the track is straight then two runners never run oast each other
#if the track is circular then the fast runner at one point crosses the slow runner and thus it proves the linked list is Circular
def circular_check(singlyLinkedList):

    runner1 = singlyLinkedList
    runner2 = singlyLinkedList
    #check until the runner2 meets the tail or right before last node
    while runner2 != None and runner2.next_Node != None:
        #set the runner1 to the next node anf fast forward the runner two by two nodes
        runner1 = runner1.next_Node
        runner2 = runner2.next_Node.next_Node

        if runner1 == runner2:
            return True
    return False        
