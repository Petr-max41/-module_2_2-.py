first = int(input('Первое число ввод '))
second = int(input('Второе  число ввод '))
third = int(input('Третье число ввод '))
if first == second == third :
    print(3)
elif first == second or first == third or second == third :
    print(2)
else:
    print(0)