# Hacker Rank Remove Duplicate Nodes

"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.

You're given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete as few nodes as possible so that the list does not contain any value more than once. The given head pointer may be null indicating that the list is empty.

"""


def RemoveDuplicates(head):
    if head == None:
        pass
    elif head.next == None:
        pass
    elif head.data != head.next.data:
        #iterate through entire linked list
        RemoveDuplicates(head.next)
    elif head.data == head.next.data:
        head.next = head.next.next
        RemoveDuplicates(head)
    return head


# With buffer
def RemoveDuplicatesV2(head):
    previous = None
    already_seen = set()
    current = head

    while current:
        # First time seeing the node
        if current.data not in already_seen:
            already_seen.add(current.data)
        else:
            previous.next = current.next

        previous = current
        current = current.next

# Without buffer
def RemoveDuplicatesV3(head):
    current = head
    while current.next:
        runner = current
        while runner.next:
            if current.value == runner.next.value:
                runner.next = runner.next.next
            else:
                runner =runner.next
        current = current.next
