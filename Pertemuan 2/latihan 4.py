# python while loops
print('while')
n = 5
while n > 0:
    n -= 1
    print(n)
print('-' * 10)
# Python breaks and continue statement
print('Break')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')
print('-' * 10)
print('Continue')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')
print('-' * 10)
print('Nested while loops')

age = 22
gender = 'M'
if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')