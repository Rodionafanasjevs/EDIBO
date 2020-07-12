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
