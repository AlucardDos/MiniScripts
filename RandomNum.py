import random
k=[0]
def rnum(a,b):
   i = random.randit(a,b)
   return i
c = input("1.Сгенерировать число \n 2.Добавить исключение \n 3.Удалить все исключения\n")
if c==2:
   k.append(input("Число: "))
if c==3:
   k.clear()
if c==1:
   print("Генерация случайного числа в диапазоне")
   a = input("От: ")
   b = input("До: ")
   j = rnum(a,b)
   while j in k:
      j = rnum(a,b)
   else:
      print(j)
      k.append(j)


   
