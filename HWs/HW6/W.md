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

---
---

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

---

name = 'Eroha'

>>> def a():

...     name = 'in a()'

def b():

...     name = 'Pupkin'

...     print(name)

...     print(locals())

  b()
  
a()

---
---

# if,boolen, else 
password = '123'

>>> user_input = '00000'

>>> if user_input == password:

...     print('Welcome')

... else:

...     print('Wrong password')

---

password = '123'

>>> user_input = '00000'

>>> if (user_input == password) or (2 * 2 == 4):

...     print('Welcome')

... else:

...     print('Wrong password')

Welcome

---

s = '12345678'

>>> if len(s) == 8:

...     print('Length 8')

... elif  len(s) == 6:

...     print('Length 6')

... else:

...     print('asff')

Length 8

 if user_input == password:
 
...     if user_input == password:

...             print('Welcome')

...     else:

...             print('Wrong password')

... else:

...     print('Input smth please')

 ---
 
... # 1 - 100

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

---
---

# Списки

l = ['a', 'b', 'c', 'd']

l

l[0] 

first = l[0]

len(l)

len(l) - 1

l[len(l)-1]

l[-2]

l[1:3]

l[1:]

l[:-1]

l[:-1:2]

l.append('e')

rl.append(l)

rl.append(l2)

['a', 'b', 'c', 'd']

rl =[]

rl

[]

rl.append(l)

rl

[['a', 'b', 'c', 'd']]

l.append('e')

rl

['a', 'b', 'c', 'd']

l

['a', 'b', 'c', 'd', 'e', 'e']

l2 = [1,2,3,4] 

---

rl.extend(l2)

rl

['a', 'b', 'c', 'd', 1, 2, 3, 4]

l.append('b')

l

---

s = 'Зайка шел гулять на речку\nперепрыгнул через речку'

s2 = s.split()

print(s2)

l = s.split('\n')

 s = ''
 
s.join(l)

'Зайка шел гулять на речкуперепрыгнул через речку'

children = ['sergeev_12', 'krukov_2323', 'Vanek_123']

s_children = sorted(children)

print(children)

['sergeev_12', 'krukov_2323', 'Vanek_123']

---

def by_year(name):

     splited_name = name.split('_')
     print(splited_name)
     
 by_year(children[0])
 
['sergeev', '12']

---

def by_year(name):

 return name.split('_')[-1] 
 
 print(by_year(children[0]))
 
12

---

def by_year(name):

return name.split('_')[-1]

 s_children = sorted(children, key=by_year)
 
print(s_children)

['sergeev_12', 'Vanek_123', 'krukov_2323']

---
---

# Цикл For

children = ['sergeev_2000', 'krukov_2002', 'Vanek_2005']

for child in children:

     print(children)
     
print(child)

names = []

for child_name in children:

     surname = child_name.split('_')[0]
     
     surname = surname.title()

---

for child_name in children:

     surname = child_name.split('_')[0]
     
     surname = surname.title()
     
     print(surname)
 
Sergeev
Krukov
Vanek

---

for child_name in children:

     surname = child_name.split('_')[0]
     
     names.append(surname)
     
     print(names)
 
['sergeev', 'krukov', 'Vanek', 'sergeev', 'krukov', 'Vanek', 'sergeev']

s = 'Hi'

 i = s.__iter__()
 
 i

---

for child_name in children:

     surname = child_name.split('_')[0]
     
     print(surname)
     
     break
     
     names.append(surname)
 
sergeev

---

for child_name in children:

     surname = child_name.split('_')[0]
     
     print(surname)
     
     break
     
     names.append(surname)
 
sergeev

---
---

# Словари

person = {'name': 'vasja', 'surname': 'pupkin', 'email': 'test@gmail.com'}

name = person['name']

 print(name)
 
vasja

tel = person.get('tel')

 print(tel)
 
None

tel = d.get('tel','12312312')

 print(tel)
 
1234

tel = person.setdefault('tel','123231')

 print(tel)
 
123231

---

for item in person.items():

     print(item)
 
('name', 'vasja')

('surname', 'pupkin')

('email', 'test@gmail.com')

('tel', '123231')

---

 for item in person:
     print(item)
 
name

surname

email

tel

---

for key, value in person.items():

print(key, value)

name vasja

---

new = {'name': 'Dima'}

 person.update(new)
 
 print(person)
 
{'name': 'Dima', 'surname': 'pupkin', 'email': 'test@gmail.com', 'tel': '123231'}
