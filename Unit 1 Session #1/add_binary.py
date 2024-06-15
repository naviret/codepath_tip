"""
Problem #3: Add Binary
Problem on Leetcode: Add Binary

Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Understand: 

  In: String
  Out: String
  
  Clarifying Q's:

  Edge cases: 
    1. If either string is empty or 0, return the non zero         string

Match:

  Use a variable to keep track of Carry,
  String/Array parsing and binary addition 

Plan: 

  # ( using Python function reverse would be O(N) )
  reverse_a 
  reverse_b 

  OR: for loop in reverse for i in range(len(max(a,b),-1,-1)

  break condition, avoid out of bounds indexing of a or b 

  # pointer for both a & b
  i = 0 
  returning_string = ""
  carry = 0 
  
  for index in range(len(max(a,b)):

    # need to check if current index is larger than b 
      # if so add just b plus carry

    # need to check if current index is larger than a 
      # if so add just a plus carry

    result = int(reverse_a[index]) + int(reverse_b[index]) +                carry
    
    if result > 1:
      carry += 1
      returning_string.append("0")
    
    else:
      returning_string.append(str(result))
  
"""
# hi lol - Ivan
# heyo d8^D - Diego
def binarysum(s1, s2):
  i = 0 
  returning_string = ""
  carry = 0 

  for index in range(len(max(s1,s2)):

    # need to check if current index is larger than b 
      # if so add just b plus carry

    # need to check if current index is larger than a 
      # if so add just a plus carry

    result = int(reverse_a[index]) + int(reverse_b[index]) +                carry

    if result > 1:
      carry += 1
      returning_string.append("0")

    else:
      returning_string.append(str(result))