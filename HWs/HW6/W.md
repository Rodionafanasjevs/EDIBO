# Funcion

def greet(name):
      print('Hello', name)
      result = 'Hello {name}'
      print(result)

greet('world')
greet('Rodion')

def greet(massage, name='world'):
...     # print('Hello', name)
...       result = f'{massage}, {name}'
...       print(result)
greet('world', name='Goodbye')
world, Goodbye

# Local name
def a():
  print(locals())

  a()

name = 'Eroha'
  name = 'Pupkin'
  print(name)

name = 'Eroha'
def a():
...     name = 'Pupkin'
...     age = 12
...     print('Funktion a() namespace:', locals())

print()

a()


name = 'Eroha'
>>> def a():
...     name = 'in a()'
def b():
...     name = 'Pupkin'
...     print(name)
...     print(locals())

  b()
a()

# if,boolen, else 
password = '123'
>>> user_input = '00000'
>>> 
>>> if user_input == password:
...     print('Welcome')
... else:
...     print('Wrong password')




password = '123'
>>> user_input = '00000'
>>> if (user_input == password) or (2 * 2 == 4):
...     print('Welcome')
... else:
...     print('Wrong password')
... 
Welcome



s = '12345678'
>>> 
>>> if len(s) == 8:
...     print('Length 8')
... elif  len(s) == 6:
...     print('Length 6')
... else:
...     print('asff')
... 
Length 8



 if user_input == password:
...     if user_input == password:
...             print('Welcome')
...     else:
...             print('Wrong password')
... else:
...     print('Input smth please')



# 1 - 100
... # 3 - Fizz
... # 5 - Bazz
...  3 & 5 - FizzBazz
def fizz_bazz(i):
...     if i % 3 == 0:
...             print('Fizz')
...     elif i % 5 == 0:
...             print('Bazz')
...     elif (i % 3 == 0) and (i % 5 == 0):
...             print('FizzBazz')
...     else:
...             print(i)
