Было замечено смещение дня весеннего равноденствия, с которым связаны церковные праздники. К XVI веку весеннее равноденствие наступало примерно на 10 суток раньше 21 марта, используемого для определения дня Пасхи.

Чтобы компенсировать накопившуюся ошибку и избежать подобного смещения в будущем, в 1582 году римский папа Григорий XIII провёл реформу календаря. Чтобы средний календарный год лучше соответствовал солнечному, было решено изменить правило високосных лет. По-прежнему високосным оставался год, номер которого кратен четырём, но исключение делалось для тех, которые были кратны 100. Такие годы были високосными только тогда, когда делились ещё и на 400.

Отсюда следует распределение високосных годов:
    
  * год, номер которого кратен 400, — високосный;
  * остальные годы, номер которых кратен 100, — невисокосные (например, го­ды 1700, 1800, 1900, 2100);
  * остальные годы, номер которых кратен 4, — високосные

# Cheet:

for leap_year in range(4,3000,4):
print(leap_year)

___

# Correct poth:

while True:
    n = int(input("leap_year: "))
    if n % 4 == 0:
        print(True)
    elif n % 100 != 0:
        print(False)
    elif n % 400 == 0:
        print(True)
    else:
        print(True)