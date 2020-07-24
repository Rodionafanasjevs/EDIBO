# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные (например, го­ды 1700, 1800, 1900, 2100);
# остальные годы, номер которых кратен 4, — високосные

# for leap_year in range(4,3000,4):
#     print(leap_year)

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