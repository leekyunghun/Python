# 자료구조 변경

menu = {"커피", "우유", "주스"} # <class 'set'>
print(menu, type(menu))

menu = list(menu)              # <class 'list'>
print(menu, type(menu))

menu = tuple(menu)             # <class 'tuple'>
print(menu, type(menu))

menu = set(menu)               # <class 'set'>
print(menu, type(menu))

from random import *
users = list(range(1, 21))
print(users)
shuffle(users)
print(users)
winners = sample(users, 4)

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print(" -- 축하드립니다 --")