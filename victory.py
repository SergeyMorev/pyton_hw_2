
name = 0
year = 1

person_list = (("Ломоносова", 1711),
               ("Менделеева", 1834),
               ("Энштейна",   1879),
               ("Ньютона",    1642),
               ("Хоккинга",   1942))
total = len(person_list)

exit_key = 'q'
res = '0'
right = 0

while (exit_key != res):
    for person in person_list:
        if input("Введите год рождения " + person[name]) == str(person[year]):
            right += 1
    print(" ----- ")
    print("Правильных ответов " + str(right))
    print("Неправильных ответов " + str(total - right))
    print("Процент правильных ответов " + str(right * 100 / total) + " %")
    print(" ----- ")
    res = input("\nДля повтора введите любой символ, для выхода введите 'q'").lower()