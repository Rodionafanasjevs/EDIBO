[Google colabe](https://colab.research.google.com/notebooks/intro.ipynb)

[Pascal's Triangle in Python](https://www.faceprep.in/python/pascal-triangle-in-python/)

[PyFormat](https://pyformat.info/PyFormatPyFormat)

In [191]: for i in range(5):
     ...:     print(11**i)
     ...:     
1
11
121
1331
14641


Vārds = "Jānis"
summa = 500000
nr = 6969696969




s = """
Godājamais %s
Jums ir pienācis naudas pārvedums
ar vērtību %d EUR
Lai saņemtu naudu atsūtiet
īsziņu uz telefona nr. %d

Cieņā,
         Atraitne.
"""  %(Vārds,summa,nr)

print(s)


#%s = string

#%d = int

Format:
name = 'Wrl'
s = 'Hi {}'
result = s.format('0')
print(result)

r = '{}'.format(name)
print(r)

l = '{}gfhgfh  {} hfgfh {}{}'.format(0, 'hi', 'ed', 32)
print(l)


newstr = f'name {s} {l}'
print(newstr)

name = 'Leon'
number = 100
pattern = '{movie} - {rating}'
result = pattern.format(movie=name, rating=number)
print(result)
