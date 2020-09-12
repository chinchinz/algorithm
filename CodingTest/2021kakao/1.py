import re

def solution(new_id):
  #1
  new_id = new_id.lower()

  #2
  new_id = re.sub(r'[^\w\-\.]', '', new_id)

  #3
  tmp_id = re.sub(r'\.\.', '.', new_id)
  while new_id != tmp_id:
    new_id = tmp_id
    tmp_id = re.sub(r'\.\.', '.', new_id)

  #4
  new_id = re.sub(r'^\.', '', new_id)
  new_id = re.sub(r'\.$', '', new_id)

  #5
  if len(new_id) == 0:
    new_id = 'a'

  #6
  if len(new_id) > 15:
    new_id = new_id[:15]
  new_id = re.sub(r'^\.', '', new_id)
  new_id = re.sub(r'\.$', '', new_id)

  #7
  while len(new_id) < 3:
    new_id = new_id + new_id[-1]
  return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))