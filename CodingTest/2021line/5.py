def solution(cards):
  ans = 0

  i = 0
  reset = True
  while i < len(cards):

    if reset:
      try:
        player = [cards[i] if cards[i] < 10 else 10, cards[i+2] if cards[i+2] < 10 else 10]
        dealer = [cards[i+1] if cards[i+1] < 10 else 10, cards[i+3] if cards[i+3] < 10 else 10]
        i += 4
        reset = False
      except:
        break
    # 플레이어 차례
    
    if sum(player) == 21 or (1 in player and 10 in player):
      # 바로 승부확인
      # print('바로 승부확인 플레이어 블랙잭')
      ans += 3
      reset = True
    else:
      # print('player')
      if dealer[1] == 1 or dealer[1] >= 7:
        while sum(player) < 17:
          player.append(cards[i])
          if(cards[i] == 1 and sum(player, 10) < 22):
            player.append(10)
          i+=1
          if i == len(cards) :
            # print('플레이어 뽑을 때 카드 없어요')
            if sum(player) < 17:
              reset = True
            break

      elif 4 <= dealer[1] <= 6:
        #카드 안받음
        pass
      elif 2 <= dealer[1] <= 3:
        while sum(player) < 12 and i < len(cards):
          player.append(cards[i])
          if(cards[i] == 1 and sum(player, 10) < 22):
            player.append(10)
          # print('플레이어 카드 계속 받는다', i)
          i+=1
          if i == len(cards) :
            # print('카드 없음 게임 그만')
            if sum(player) < 12:
              reset = True
            break

      if sum(player) > 21:
        #즉시 패배
        ans -= 2
        reset = True
        # print('플레이어 바로 패배 21초과')

    # print('딜러 차례')

    if sum(dealer) == 21 or (1 in dealer and 10 in dealer):
      # 바로 승부확인
      # print('바로 승부확인 딜러 블랙잭')
      pass

    elif not reset and i < len(cards):
      while sum(dealer) < 17:
        # print('계속 받는다', i, cards)
        dealer.append(cards[i])
        if(cards[i] == 1 and sum(dealer, 10) < 22):
            dealer.append(10)
        i+=1
        if sum(dealer) > 21:
          # print('딜러 21초과 딜러 패배')
          ans += 2
          reset = True
        if i == len(cards) :
          # print('딜러 뽑을 때 카드 없어요')
          if sum(dealer) < 17:
            reset = True
          break


    if not reset:
      if 1 in dealer and sum(dealer) < 12:
        dealer.append(10)
      
      if 1 in player and sum(player) < 12:
        player.append(10)
      
      # print('결과:', sum(player), sum(dealer))
      if sum(player) > sum(dealer):
        ans += 2
      elif sum(dealer) > sum(player):
        ans -= 2
      reset = True  
    # print('현재 스코어 : ', ans)
  return ans


# print('-------------new game--------------')
print(solution([12, 7, 11, 6, 2, 12]))
# print('-------------new game--------------')
print(solution([1, 4, 10, 6, 9, 1, 8, 13]	))
# print('-------------new game--------------')
print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))
# print('-------------new game--------------')
print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))