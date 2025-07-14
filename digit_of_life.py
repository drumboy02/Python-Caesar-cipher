#!/usr/bin/env python3

date = ''

def dig_of_life(date):
  # output the Digit of Life for the data
  res = sum([int(d) for d in date])

  while res > 9:
    res = str(res)
    res = sum([int(d) for d in res])

  return res

while not date:
  # ask the user for their birthday in format (YYYYMMDD, YYYYDDMM, or MMDDYYYY)
  date = input("Enter your birthday: ")
  if len(date) != 8:
    date = ''
  try:
    int(date)
  except ValueError:
    print("You must enter YYYYMMDD, YYYYDDMM or MMDDYYYY format")
    date = ''
    
print("Digit of Life:", dig_of_life(date))
