import math

def is_palindromic(n): 
  return str(n) == str(n)[::-1]
  
def double_palindromes(n):
  dec2bin = lambda n: str(bin(n))[2:]
  total_sum = 0
  for i in range(1,n):
    if is_palindromic(i) and is_palindromic(dec2bin(i)):
      total_sum += i
  return total_sum

print double_palindromes(1000000)