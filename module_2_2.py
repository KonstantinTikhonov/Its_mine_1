first = input('Input first:')
second = input('Input second:')
third = input('Input third:')
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
# мы сравниваем строки,
# если нужно сравнить числа, то используем int(first), int(second), int(third)
