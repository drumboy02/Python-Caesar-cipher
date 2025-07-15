#!/usr/bin/env python3

puzzleY = '''295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
'''

puzzleN = '''195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
'''

def chk_row(puzzle):
  puzzle = puzzle.replace('\n', '')
  row = 9
  idx = 0
  
  for i in range(row):
    r = puzzle[idx:idx + row]
    nums = [n for n in range(1, 10)]
    
    for ch in r:
      ch = int(ch)
      
      if ch in nums:
        del nums[nums.index(ch)]
        # print('nums', nums)

    if nums == []:
      nums = [n for n in range(1, 10)]
    else:
      return False

    idx += row

  return True


def chk_col(puzzle):
  puzzle = puzzle.replace('\n', '')
  col = 9
  idx = 0

  for i in range(col):
    c = puzzle[idx::col]
    nums = [n for n in range(1, 10)]

    for ch in c:
      ch = int(ch)

      if ch in nums:
        del nums[nums.index(ch)]
        # print('nums', nums)

    if nums == []:
      nums = [n for n in range(1, 10)]
    else:
      return False
    
    idx += 1

  return True

def chk_sq(puzzle):
  puzzle = puzzle.replace('\n', '')
  
  for i in range(3):
    st = i * 27
    ed = i * 27 + 3
    
    for j in range(3):
      sq = puzzle[st:ed] + puzzle[st+9:ed+9] + puzzle[st+18:ed+18]
      nums = [n for n in range(1, 10)]
      
      for ch in sq:
        ch = int(ch)

        if ch in nums:
          del nums[nums.index(ch)]
          # print(nums)

      if nums == []:
        nums = [n for n in range(1, 10)]
      else:
        return False
      
      st += 3
      ed += 3

  return True

def solved(puzzle):
  print(puzzle)
  # output Yes if Sudoku is valid, No otherwise
  if chk_row(puzzle) and chk_col(puzzle) and chk_sq(puzzle):
    return "Yes"
  else:
    return "No"

print('Sudoku is valid?', solved(puzzleY))
print()
print('Sudoku is valid?', solved(puzzleN))
