#1. Функция сумира всички сисла в масив
a = [1,2,3,4,5]

def sum(numbers):
   result = 0
   for item in numbers:
      result = result + item
   return result

sumRes = sum(a)
print(sumRes) # 15
