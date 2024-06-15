"""
Problem #1: Substring

Write a function that takes in two strings and returns True if the second string is a substring of the first, and False otherwise.

NOTE: You may not use the in operator (Python) or call a library function that tests for substrings, such as substring() or indexOf() (Java).


Example 1:
Input: laboratory, rat
Output: true

Example 2:
Input: cat, meow
Output: false


Understand:

  Edge case:
    1. if the second substring is empty then its substring of all strings
    2. if second string is longer than first string you return false
    3. invalid input (not a string)
    4. first string is exactly the same as second string

  Input:
    two strings

  Output:
    boolean
    whether second string is subtring of first


Match:

  string/array and python splicing

Plan:

  substring 456
  string 123457

  i = 3
  j = 0

  i = 4
  j = 1

  i = 5
  j = 2

  break condition when 
  if j = len(substring) - 1
    return True
  
  
  m = len(first_string)
  n = len(second_string)
  Time Complexity = O(mn)

    
  looking for the first character in the substring in string
    once you find a match, 
      splice the original string with the length of second string

Implement:


Review:

  the j - 1, changed order of if statements so that i and j are at same spot

Evaluate:

  Time complexity: O(n)
    n = length of s1
    m = length of s2
      - no nested for loops

  Space complexity: O(1)
  
"""


def isSubstring(s1, s2):

  if s2 == "":
    return True

  if len(s2) > len(s1):
    return False

  j = 0
  for i in range(len(s1)):

    if s1[i] == s2[j]:
      j += 1
    else:
      j = 0

    if j == len(s2):
      return True

  return False


print(isSubstring("ctcat", "cat"))
  