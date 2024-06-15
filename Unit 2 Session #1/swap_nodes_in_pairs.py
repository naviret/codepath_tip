"""
Problem 1: Swap Nodes In Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Image of example #1 linked lists
Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = [ ]
Output: [ ]
Example 3:

Input: head = [1]
Output: [1]

Understand:
  Assuming singly linked list.

  - Edge cases:
    empty linked list: just return head that was passed in 
    linked list with one item: return head
    Odd number of items: only swap those who don't point to null       aka ([1,2,3] -> [2,1,3] since 3 points to null)

      H T
  R
  2 1 3 4
  

Match:

  - Two pointer: 
  - Temp head: store the rest of the linked list from second node in pair, and move head to remainder of list. 
  ** Make sure to hold a reference to the head of the linked list for return purposes

Plan:

  Inputs: head of linked list 
  Output: head of reordered linked list 
                     n  t
  To Do iteratively: 1, 2 3 [ 1 -> 3 , 2 -> 3, 2->1->3]
    * temp = node.next 
    * node.next = node.next.next
    * temp.next = node 
  
   temp = node.next.next 
   node = node.next
    
   1 2 3  
  
  if len(list) > 2:
    ret_head = head.next 

  # continue to iterate afterwards 
  while temp: 
    temp = node.next 
    node.next = node.next.next
    temp.next = node

    # for shifting pointers over 
    temp = node.next.next 
    node = node.next
  
  return ret_head 

Implementation: GET IT TO WORK!


Review: Linear time complexity = O(N), space complexity = O(1)

"""

import re


def findLength(head):

  i = 0
  while head:
    head = head.next
    i += 1

  return i

#

# i think we just need to make sure that
# there's something after the 1

# do example with 1 2 i think


def swap_pairs(head):

  if head is None or head.next is None:
    return head

  # running on 1 -> 2
  node = head  # node = 1
  temp = head.next  # temp = 2
  ret_head = temp  # returning 2

  # continue to iterate afterwards
  while temp and node:
    
    temp = node.next  # temp = 2
    node.next = node.next.next  # 1 -> null
    temp.next = node  # 2 -> 1

    print("temp:", temp.val)
    print("node:",node.val)

    temp = node.next.next
    # i got it to run but its wrong
    # yea i see 

    # d8^D 
    # yea lol bet same :}
    
    # if theres a node after assign temp
    # to it
    if node.next:
      temp = node.next.next

    # ran it but there's still an issue with line 116
    # hmmmmm
    #
    node = node.next

  return ret_head


def printList(head):

  while head:
    print(head.val, end=" ")
    head = head.next

  print("")


class Node():

  def __init__(self, val, next) -> None:
    self.val = val
    self.next = next


list = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
printList(swap_pairs(list))

# list2 = Node(0, Node(1, Node(2, None)))
# printList(swap_pairs(list2))

# list3 = Node(1, Node(2, Node(3, Node(4, None))))
# printList(swap_pairs(list3))
