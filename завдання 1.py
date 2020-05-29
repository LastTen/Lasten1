name_us = str(input( '''введіть ваше ім\'я '''))
stored_pass = '123'
m = 0
n = 0
print('Введіть пароль')
while m <= 2:
    n = str(input('Gfhjkmf'))
    m = m+1
    if stored_pass == n:
        print('Вітаю ' + str(name_us))
        while True:            
            first_operand = float(input('first_operand='))
            operator = str(input('дія '))
            second_operand = float(input('second_operand='))
            if first_operand == 0 or  second_operand == 0:
                break
            elif operator == '+':
                result = (first_operand+second_operand)
                print ('answer'   + str(result))
            elif operator == '-':
                result = (first_operand-second_operand)
                print ('answer'   + str(result))
            elif operator == '*':
                result = (first_operand*second_operand)
                print ('answer'   + str(result))
            elif operator == '/':
                result = (first_operand/second_operand)
                print ('answer '   + str(result))
            else:
                print(" невірна дія ")
        
    if not n == stored_pass:
        print("не верно повторите ввод")
    if m == 2:
        print("lock") 