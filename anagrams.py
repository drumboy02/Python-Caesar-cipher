#!/usr/bin/env python3

text1, text2 = '', ''

def anagrams(text1, text2):
  # check if entered texts are anagrams
  nspc1, nspc2 = text1.replace(' ', '').lower(), text2.replace(' ', '').lower()
  
  if len(nspc1) != len(nspc2):
    return "Not anagrams"
  
  for c in nspc1:
    if c not in nspc2:
      return "Not anagrams"

  return "Anagrams"

# asks the user for two seperate texts
while not text1:
  text1 = input("Enter the first word: ")
  if not text1:
    continue
while not text2:
  text2 = input("Enter the second word: ")
  if not text2:
    continue

# print the result
print(anagrams(text1, text2))
