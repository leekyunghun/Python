# 한 줄 반복문
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

from random import *

count = 0
for i in range(50):
    minutes = randint(5, 50)
    if minutes <= 15 and minutes >= 5:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(i+1, minutes))
        count += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(i+1, minutes))

print("총 탑승 승객 : {} 분".format(count))