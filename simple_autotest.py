from functions import salary, hello_who

assert hello_who('Max') != 'Hello,Max', 'Error with Max'
assert hello_who('Leo') != 'Hello,Leo', 'Error with Leo'
assert hello_who('Nikita') != 'Hello,Nikita', 'Error with Nikita'
assert salary(2, 1) == 4
assert salary(2, 2) == 8