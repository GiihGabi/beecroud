from random import randint

num = []

for i in range(0,10):
  num.append(randint(0,100))
print(num)
for a in range(len(num)):
  if a == len(num) - 1:
    print(num[a])
  else:
    print(num[a] + num[a + 1])