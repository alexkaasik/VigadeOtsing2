print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Введите целое число => ")))) # change )) to ))))
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a # change == to =
    paaris = 0 # change == to =
    paaritu = 0 # change == to =

    while b > 0: # change ; to :
            if b % 2 == 0: # change = to ==
                    paaris += 1 # change =+ to +=
            else:
                    paaritu += 1 # change =+ to +=
            b = b // 10 # remove extra tab
    
    print("Чётных цифр:",paaris) # added a , before variable
    print("Нечётных цифр:",paaritu) # added a , before variable
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    
    b=0
    while a > 0: # added a missing :
        number = a % 10
        a = a // 10
        b = b * 10
        b += number # removed extra space and change =+ to +=
    print("*Перевёрнутое* число", b)
    print()
 #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз") # removed extra (
    print()
    if c % 2 == 0: # change = to ==
        print(f"{c} - чётное число. Делим на 2.") # change to "с to f"{c}
    else:
        print(f"{c} - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.") # change to "с to f"{c}
    while c != 1:
            if c % 2 == 0: # change = to ==
                    c = c / 2 # change == to =
            else:
                    c = (3*c + 1) / 2 # change == to =
            print(int(c), end=" ") # change " to " " and added int() to c
    print()
    print("Гипотеза верна") # change '' to "