"""
Problem #1: Integer Replacement

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.
Tip: Java programmers should treat Integer.MAX_VALUE() as a special case.


Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:
Input: n = 4
Output: 2

Example 4:
Input: n = 14
Output: 5

14 -> 7 -> 8 -> 4 -> 2 -> 1

Example 5:
Input: n = 11
Output: 5

11 -> 10 -> 5 -> 4 -> 2 -> 1
11 -> 12 -> 6 -> 3 -> 2 -> 1

Example 6:
Input: n = 3
Output: 2

3 -> 4 -> 2 -> 1
3 -> 2 -> 1


Understand:
n is greater than or equal to 1
If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Match:
1. Greedy Algorithm
2. Memoization -> Recursion - break out n into smaller subproblems

Plan:
1. Base Case: n == 1 return 0
2. min_Ops = 0
3. while n > 1 -> breakout condition
4. If n % 2 == 0:
    min_Ops += recursion(n//2)
5. Else
    min_Ops + min(recursion(n+1), recursion(n-1))
6. 
 
// base: n == 1 return 0
// if even: return 1 + rec(n//2)
// else: return 1 + min(rec(n+1), rec(n-1))

"""
memo = dict()
def int_replacement(n):
  if n == 1:
    return 0
    
  if n in memo:
    return memo[n]
    
  if (n % 2) == 0:
    memo[n] = 1 + int_replacement(n/2)
  else:
    memo[n] = 1 + min(int_replacement(n+1), int_replacement(n-1))

  return memo[n]



print(int_replacement(14))
print(int_replacement(11))
print(int_replacement(8))
print(int_replacement(1))
print(int_replacement(2))
print(int_replacement(2140000000))
print(int_replacement(4294967296))
