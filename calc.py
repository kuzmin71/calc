from math import sqrt
print('Калькулируйте')
print('(Чтобы завершить программу, пропишите в "Типе операции" слово "end")')

while True:

    first_number = float(input('Первое число: '))
    second_number = float(input('Второе число: '))
    type_of_transaction = input('Тип операции(*,/,+,-,^,sqrt): ')

    fn = first_number
    sn = second_number
    tot = type_of_transaction

    if tot == '*':
        print(fn*sn)
    elif tot == '/':
        print(fn/sn)
    elif tot == '+':
        print(fn+sn)
    elif tot == '-':
        print(fn-sn)
    elif tot == '^':
        print(fn**sn)
    elif tot == 'sqrt':
        tot1 = input('Выберите знак между числами(*,/,+,-,^)')
        if tot1 == '*':
            print(sqrt(fn*sn))
        if tot1 == '/':
            print(sqrt(fn/sn))
        if tot1 == '+':
            print(sqrt(fn+sn))
        if tot1 == '-':
            print(sqrt(fn-sn))
        if tot1 == '^':
            print(sqrt(fn**sn))

    if tot == 'end':
        break
else:
    print('не понимаю, попробуй еще раз')

print('Спасибо, что воспользовались этой программой')