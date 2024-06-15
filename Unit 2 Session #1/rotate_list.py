"""
Problem 2: Rotate List
Original Problem on Leetcode: Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example of odd even linked list
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example of odd even linked list
Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Input: head = [1,2,3,4], k = 2
Output: [3,4,1,2]

Understand:

  goal is to shift nodes right k times

  singly linked list

  Edge cases:
    empty list? return head
    one single node? return head as well

  Assumptions:
    k is a positive integer
      no zeros

      if k was zero we return the head


Match:

  temp nodes
  
  Strategies:
    rotate manually
    
    manipulate the pointers
    [1,2,3,4,5] 
    k = 2
    n = 5
    n - k = 3
  
    head = 1, 2, 3 becomes the last 
    temp = 4, 5 becomes the beginning


Plan:

  input:
    head
    k

    # write a function to find length
    n = len(list)
    k %= n
        
    if k == 0 or n <= 1:
      return head

    temp = head
    for i in range(n - k - 1):
      temp = temp.next
      
    temp.next, temp = None, temp.next

    new_head = temp
    for i in range(k - 1):
      temp = temp.next 

    temp.next = head

    return new_head

Review:

  Time complexity:
    O(N)

  Space complexity:
    O(1)

"""


def findLength(head):

  i = 0
  while head:
    head = head.next
    i += 1

  return i
  

def rotateList(head, k):

  n = findLength(head)
  k %= n

  if k == 0 or n <= 1:
    return head

  temp = head
  for _ in range(n - k - 1):
    temp = temp.next

  temp.next, temp = None, temp.next

  new_head = temp
  for _ in range(k - 1):
    temp = temp.next 

  temp.next = head

  return new_head

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

printList(rotateList(list, 2))

list2 = Node(0, Node(1, Node(2, None)))
printList(rotateList(list2, 4))

list3 = Node(1, Node(2, Node(3, Node(4, None))))
printList(rotateList(list3, 2))
