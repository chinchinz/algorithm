def solution(phone_book):
  d = {}
  phone_book.sort(key=lambda x : len(x))
  for number in phone_book:
    for key in d.keys():
      # print(number, key)
      if number.startswith(key): return False
    d[number] = True
  return True

print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))