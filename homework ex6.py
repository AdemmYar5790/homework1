#Задача 6: Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
#километров. Каждый день спортсмен увеличивал результат на 10% относительно
#предыдущего. Требуется определить номер дня, на который результат спортсмена составит не
#менее b километров. Программа должна принимать значения параметров a и b и выводить
#одно натуральное число — номер дня

g = float(input("Enter start: "))
h = int(input("Enter finish: "))
day = 1
if g > h:
    print(day)
while g < h:
    g = g + g / 10
    day += 1
print(day)
