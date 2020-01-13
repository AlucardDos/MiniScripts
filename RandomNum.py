import random
l = True
while l:
   k=[0]
   def rnum(a,b):
      i = random.randint(a,b)
      return i
   print("1.Сгенерировать число")
   print("2.Добавить исключение")
   print("3.Удалить все исключения")
   print("4.Выход")
   c =int( input())
   if c==1:
      print("Генерация случайного числа в диапазоне")
      a =int(input("От: "))
      b = int(input("До: "))
      j =int( rnum(a,b))
      x=True
      while x:
      	if j in k:
      		j= rnum(a,b)
      	else:
      		x=False
      print("Число: " + j)
   if c==4:
      	l=False
   if c==2:
   	k.append(input("Число: "))
   if c==3:
   	k.clear()
   if c==4:
   	l = False