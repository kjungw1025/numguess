# 문을 바꿨을 때 이길 확률과 안 바꿨을 때 이길 확률 시뮬레이션
from random import shuffle, choice

stay = 0
change = 0

n = int(input("How many times you want for simulation? "))

# 염소 : 0, 스포츠카 : 1
for _ in range(n):
  doors = [0, 0, 1]
  # 문안에 염소, 스포츠카 위치 결정됨 (고정)
  shuffle(doors)
  # 선택자가 문을 고름
  sel = doors.pop()
  # 진행자가 염소가 있는 문중에 하나를 열어서 보여줘야하므로 doors에 있는 0을 지움
  doors.remove(0)
  if sel == 1:  # 선택자가 1인 문을 선택했었다면 stay
    stay += 1
  else:         # 그게 아니라면 change 해야함
    change += 1
print("stay: "+ str(stay) + " " + "change: " + str(change))

