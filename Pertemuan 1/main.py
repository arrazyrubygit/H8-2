#integer
print('-' * 30)
print('INTEGER')
print('-' * 30)
print(123123123123123123123123123123123123123123123123 + 1)

# Python interprets a sequence of decimal digits without any prefix to be a decimal number:
print(10)
print(type(10))

#floating numbers
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)
print('-' * 30)
#strings
print('STRINGS')
print('-' * 30)
print("Hacktiv8")
print(type("Hacktiv8"))

print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')
print('-' * 30)
#boolean type
print('BOOLEAN')
print('-' * 30)
print(type(True))
print(type(False))
print('-' * 30)
#variable assignment
print('VARIABLE ASSIGNMENT')
print('-' * 30)
n = 300
print(n)

# Ubah besaran nilai N maka nilainya akan berubah:
n = 1000
print(n)
n

a = b = c = 1200
print(a, b, c)

#variable types in python
var = 23.5
print(var)

var = "Now I'm a string"
print(var)

#variable names
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)

#python case sensitive : penggunaan huruf harus benar besar/kecilnya
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)
# ada 3 metode penulisan multivariable
# 1.Camel case : numberOfCollegeGraduates
# 2.Pascal case : NumberOfCollegeGraduates
# 3.Snake case : number_of_college_graduates
print('-' * 30)
#Operators and Expresion in Python
print('OPERATOR AND EXPRESION')
print('-' * 30)
a = 10
b = 20
a + b

a = 10
b = 20
a + b - 5

#arithmetics operator
a = 4
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

10 / 5
#hasil dari pembagian selalu float

#comparison operator
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

a = 30
b = 30
print(a == b)
print(a <= b)
print(a >= b)
print('-' * 30)
#string manipulation
print('STRING MANIPULATION')
print('-' * 30)
# + Operators
s = 'foo'
t = 'bar'
u = 'baz'

print(s + t)
print(s + t + u)
print('Hacktiv8 ' + 'PTP')

# * Operators
s = 'foo.'
s * 4


# in Operators
s = 'foo'
print(s in 'That food for us')
print(s in 'That good for us')

# Case Conversion
s = 'HackTIV8'
# Capitalize
print(s.capitalize())
# Lower
print(s.lower())
# Swapcase
print(s.swapcase())
# Title
print(s.title())
# Uppercase
print(s.upper())
print('-' * 30)

#Python list
print('PYTHON LIST')
print('-' * 30)
a = ['foo', 'bar', 'baz', 'qux']
print(a)

#list berurutan
a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']

a == b

#list bisa dalam berbagai macam tipe
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a)

#list elemen dapat diakses dengan indeks
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0])
print(a[5])
print('Urutan dengan index negatif')
print(a[-1])
print(a[-6])
print('Slicing dengan ekspresi a[m:n]')
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2:5]

# The concatenation (+) and replication (*) operators:
print(a)
print(a + ['grault', 'garply'])
print(a * 2)

# len(), min(), max()
print(a)

print(len(a))
print(min(a))
print(max(a))

#Modifying a Single List Value
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
a[2] = 10
a[-1] = 20
print(a)

# A list item can be deleted with the del command:
del a[3]
print(a)

#Modifying Multiple List Values
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)
print('-' * 30)
print('TUPLE')
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print('-' * 30)