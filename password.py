cod=3458 #код
counter=0 #счетчик попыток
pass_us=0
print("введите код, после третеи попытки замок заблокируется")
while counter<=3:
    pass_us=int(input()) #ввод с клавиатуры
    counter=counter+1
    if pass_us==cod:
        print("open")
        break;
    if not pass_us==cod:
        print("не верно повторите ввод")
    if counter==3:
        print("lock") # число попыток превышено, замок заблокирован