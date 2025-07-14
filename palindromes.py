#!/usr/bin/env python3

text = ''

def chk_palindrome(text):
  # check whether the entered text is a palindrome
  lst = text.lower().strip().split(' ')
  s = ''.join(lst)
  
  for c in range(len(s)):
    if s[c] != s[len(s) - c - 1]:
      return "It's not a palindrome"
    
  return "It's a palindrome"

while not text:
  # ask user for some text
  text = input("Enter text: ")
  
# print the result
print(chk_palindrome(text))
