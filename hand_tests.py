from functions import salary, hello_who

# print(hello_who('Anton'))
# print('Your salary:', salary(2, 10))

if salary != 20:
    print('Error')

if hello_who('Max') != 'Hello, Max':
    print('Failed - 1.1.')
else:
    print('Good')

if hello_who('Leo') != 'Hello, Leo':
    print('Failed - 1.2.')
else:
    print('Amazing')

if hello_who('Anton') != 'Hello, Anton':
    print('Failed - 1.3.')
else:
    print('Woow!')

if hello_who('John') == 'Hello, Max':
    print('Failed - 1.4.')
else:
    print('All good')