class Node:
    pass

node_start,node_end = None, None

def createNode(node_start,node_end):
    node1 = Node()
    node1.data = input("Enter data to insert in linked list")
    node1.next = None
    if(node_start==None):
        node_start = node1
        node_end = node1
    else:
        node_end.next = node1
        node_end = node1
    return (node_start,node_end)
            
def printLinkedList(node_start):
    tempNode = node_start
    while(tempNode!=None):
        print(tempNode.data)
        tempNode = tempNode.next
    
while(True):
    print("Enter 1 to add data in linked list and 0 to stop adding to the linked list")
    check_val = int(input())
    if(check_val==0):
        break
    if(check_val==1):
        node_start,node_end = createNode(node_start,node_end)

printLinkedList(node_start)
