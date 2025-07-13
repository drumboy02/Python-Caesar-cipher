#!/usr/bin/env python3

while True:
  # ask the user for one line of text to encrypt
  text = input("Enter one line of text to encrypt: ")
  if len(text) == 0:
    continue
  
  try:
    # ask the user for a shift value (1 - 25). validate
    shift = int(input("Enter a shift value 1-25: "))
    if shift < 1 or shift > 25:
      print("Shift value must be a number between 1 and 25")
      continue
    else:
      break
  except ValueError:
    print("Shift value must be a number between 1 and 25")
    continue

def caesar(text, shift):
  enctext = ''
  
  for c in text:
    if not c.isalpha():
      enctext += c
    else:
      code = ord(c) + shift
      
      if c.isupper():
        if code > ord('Z'):
          code = (code - ord('Z')) + ord('A') - 1
      elif c.islower():
        if code > ord('z'):
          code = (code - ord('z')) + ord('a') - 1
          
      enctext += chr(code)

  return enctext

# print out the encoded text
print(caesar(text, shift))
