#!/usr/bin/env python3

def find_word(word, string):
  found = ''
  idx = 0

  for c in word:
    test = string.upper().find(c.upper(), idx)
    if test > -1:
      idx = test + 1
      found = "Yes"
    else:
      found = "No"
      break

  return found

word, string = '', ''

while not string:
  string = input("Enter a string: ")
  if len(string) < 1:
    continue
  
  while not word:
    word = input("Enter the hidden word: ")

# are the characters comprising the first string hidden inside the second string?
print(f'{word} hidden in {string}?', find_word(word, string))
