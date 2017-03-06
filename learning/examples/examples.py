# arithmetic expressions
x = 30
y = x ** 2
print(y)

w = y * 3.75
print(w)


# if statement
hello_world = True
if hello_world:
    print("IF is true")

x = 0
if x < 0:
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# strings
print(3 * "un" + "ium")  # unununium
textNewLine = ("Put several strings within parentheses "
               "to have them joined together.")
print(textNewLine)
textNewLine += " blah blah blah"
print(textNewLine)
word = "home"
print(word[0])
print(word[3])
print(word[-1])
print(word[0:2])
print(word[:2])
print(word[2:])
print(len(word))


# lists
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[-1])
print(squares[-3:])
squares2 = squares + [36, 49, 64, 81, 100]
print(squares2)
squares2[0] = 1000
print(squares2)
squares2.append(2000)
print(squares2)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(len(letters))
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(len(x))
print(x[0])
print(x[0][1])
x = a + n
print(x)


# for
nomes = ['casa', 'açougue', 'ameixa']
for nome in nomes:
    print(nome, len(nome))


# cria uma cópia da lista
for nome in nomes[:]:
    if len(nome) > 7:
        nomes.insert(0, nome)
print(nomes)  # lista preservada


# range(10) == range(0,10)
for i in range(0, 10):
    print(i, end=' ')
print('\n')

for i in range(len(nomes)):
    print(nomes[i])


# pass (não faz nada, só para completar sintaxe)
def func():
    pass  # Remember to implement this!


# Functions
def fatorial(numero):
    """Calcula o fatorial de seu número"""
    fat = 1
    if numero > 0:
        for cont in range(1, numero + 1):
            fat *= cont
        print('Fatorial de ', numero, '-', fat)
    else:
        print('Não é possível calcular o fatorial')
fatorial(-1)
fatorial(4)
print(fatorial)
funcao = fatorial
funcao(5)
print(fatorial(10))


# Functions with return
def calcula_fatorial(numero):
    """===Cálculo de fatorial===

Calcula o fatorial de seu número e retorna o resultado"""
    fat = 1
    if numero > 0:
        for cont in range(1, numero + 1):
            fat *= cont
        return fat
    else:
        return 0
a = calcula_fatorial(10)
print('Fatorial -', a)
print(calcula_fatorial.__doc__)


# Functions default values
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    """Lê o valor do teclado e determina se é sim ou não"""
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i=5


def f(arg=i):  # o valor default de arg sempre será avaliado como 5
    print(arg)
i=6
f()


# o valor default só é avaliado uma única vez
def f(a, l=[]):
    l.append(a)
    return l
print(f(1))
print(f(2))
print(f(3))


# valor default sempre vazio durante a chamada
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f2(1))
print(f2(2))
print(f2(3))


# keyword arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# but all the following calls would be invalid:
# parrot() - required argument missing
# parrot(voltage=5.0, 'dead') - non-keyword argument after a keyword argument
# parrot(110, voltage=220) - duplicate value for the same argument
# parrot(actor='John Cleese') - unknown keyword argument


# unpacking arguments
args = [3, 6]
lista = list(range(*args))
print(lista)

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# dynamic arguments and keywords
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# arbitrary argument lists
def concat(*args, sep="/"):
    return sep.join(args)
print(concat("earth", "mars", "venus"))

# lambda expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(make_incrementor(42))
print(f(2))


# lists
squares = [x**2 for x in range(10)]
print(squares)

lista = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(lista)

vec = [-4, -2, 0, 2, 4]
lista = [x*2 for x in vec]
print(lista)

freshfruit = [' banana', ' loganberry ', 'passion fruit ']
lista = [weapon.strip() for weapon in freshfruit]
print(lista)

lista = [(x, x**2) for x in range(6)]
print(lista)

from math import pi
lista = [str(round(pi, i)) for i in range(1, 6)]
print(lista)

m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matriz = [[row[i] for row in m] for i in range(4)]
print(matriz)

copia = []
for i in range(4):
    copia.append([row[i] for row in m])
print(copia)

# criando lista a partir de vetor/matriz
lista_copia = list(zip(*copia))
print(lista_copia)

del lista_copia[:]
print(lista_copia)


# tuples (OBS: tuples are immutable)
t = 12345, 54321, 'hello!'
print(t[0])

u = t, (1, 2, 3, 4, 5)
print(u)


# sets: an unordered collection with no duplicate elements
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

resultado = 'orange' in basket
print(resultado)

a = set('abracadabra') # unique letters in a
print(a)

b = set('alacazam')
print(a - b)  # letters in a but not in b
print(a | b)  # letters in either a or b
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both

# set comprehensions, as list comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


# dictionaries
tel = {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['guido'])
print(tel)

del tel['sape']
print(tel)

print(list(tel.keys()))
print(sorted(tel.keys()))

res = 'guido' in tel
print(res)

res = 'jack' not in tel
print(res)

dicionario = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dicionario)

dic = {x: x**2 for x in (2, 4, 6)}  # dict comprehensions
print(dic)

dic = dict(sape=4139, guido=4127, jack=4098)
print(dic)

for k, v in dic.items():
    print(k, v)

from learning.functions import function_examples
data = function_examples.concat_datas('03', '03', '1989')
print(data)

print(dir())

# input and output
s = 'Hello world!'
print(str(s))

print(str(1/7))

# print alignment
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('12'.zfill(5))

print('-3.14'.zfill(7))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

import math
# ’!a’ (apply ascii()), ’!s’ (apply str()) and ’!r’ (apply repr()) can be used to convert the value before it is formatted
print('The value of PI is approximately {!r}.'.format(math.pi))

print('The value of PI is approximately {0:.3f}.'.format(math.pi))

# Passing an integer after the ’:’ will cause that field to be a minimum number of characters wide. This is useful for making tables pretty.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))


for x in range(0,6):
    print(x)

# files
# ’r’ when the file will only be read;
# ’w’ for only writing (an existing file with the same name will be erased);
# ’a’ opens the file for appending; any data written to the file is automatically added to the end;
# ’r+’ opens the file for both reading and writing. The mode argument is optional; and
# ’r’ will be assumed if it’s omitted.
f = open('arquivoteste.txt', 'r')

for line in f:
    print(line, end='')

f2 = open('arquivoteste.txt', 'a')
f2.write('\nThis is a test\n')

f = open('arquivoteste2.txt', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5) # Go to the 6th byte in the file 5
print(f.read(1))
f.seek(-3, 2) # Go to the 3rd byte before the end 13
print(f.read(1))

f.close()
f2.close()

with open('arquivoteste.txt', 'r') as f:
    read_data = f.read()
print(f.closed)
print(read_data)

# JSON support
import json

print(json.dumps([1, 'simple', 'list']))

file_json = open('arquivo_com_json.txt', 'w')
json.dump([1, 'simple', 'list'], file_json)
file_json.close()

read_json = open('arquivo_com_json.txt', 'r')
lista = json.load(read_json)
for x in lista:
    print(x)

# handling dictionaries with json
file_json = open('arquivo_com_json.txt', 'w')
json.dump({'jack': 4098, 'sape': 4139}, file_json)
file_json.close()

read_json = open('arquivo_com_json.txt', 'r')
dicionario = json.load(read_json)
for x, y in dicionario.items():
    print(x, y)

# exceptions
# while True:
#    try:
#        x = int(input("Please enter a number: "))
#        break
#    except ValueError:
#        print("Oops! That was no valid number. Try again...") # or "pass"

# raise exception
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# instance.args within an exception
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    x, y = inst.args
    print('x =', x)
    print('y =', y)

# raising exception
# raise NameError('HiThere')

# user-defined exceptions
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

# clean-up actions
# try:
#    raise KeyboardInterrupt
# finally:
#    print('Goodbye, world!')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2,1)
divide(2,0)

# scopes and namespaces

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)

# classes

class MyClass:
    """A simple example class"""

    def __init__(self, ivalue):
        self.data = []
        self.i = ivalue

    def f(self):
        return 'hello world'

x = MyClass(0)
print(x.i)
print(x.f())
print(x.__doc__)

y = MyClass(2)
print(y.i)

# data attributes
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
    print(x.counter)
del x.counter

# class and instance variables


class Dog:

    kind = 'canine' # class variable shared by all instances

    def __init__(self, name):
        self.name = name # instance variable unique to each instance
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
d.add_trick('roll over')

e = Dog('Buddy')
e.add_trick('play dead')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
print(d.tricks)
print(e.tricks)

# inheritance


class Mapping:
    def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original update() method


class MappingSubclass(Mapping):
    # provides new signature for update()
    # but does not break __init__()
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


# "structs"
class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# iterators
for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one':1, 'two':2}:
    print(key)

for char in "123": print(char)

# for line in open("myfile.txt"):
#    print(line, end='')


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char)


# generators as quick iterators
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# operating system commands
import os
print(os.getcwd())

# the shutil module provides a higher level interface that is easier to use
import shutil
shutil.copyfile('arquivoteste.txt', 'teste.txt')

# the glob module provides a function for making file lists from directory wildcard searches
import glob
print(glob.glob('*.py'))

# command line arguments
import sys
print(sys.argv)

# string patterns
import re

res = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(res)

res = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(res)

str = 'tea for too'.replace('too', 'two')
print(str)

# internet access

# URL
# from urllib.request import urlopen

# SMTP
# import smtplib

# date and time
from datetime import date
now = date.today()
print(now)

formatted = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(formatted)

birthday = date(1989, 3, 3) # (year, month, day)
age = now - birthday
print(age.days)

# data compression
import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))

# performance measurement
from timeit import Timer

x = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(x)

y = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(y)


# testing
def average(values):
    return sum(values) / len(values)

import unittest


class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

# Calling from the command line invokes all tests
# unittest.experiment()

# logging
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')