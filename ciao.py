print("Ciao, inserisci un numero: ")

a = int(input())

if a > 10:
    print("Hai inserito un numero maggiore di 10!")

print("Addio")

# commento

x = 1
if x == 1:
    print("x is 1")

myInt = 7

myFloat = 7.0
myFloat1 = float(myInt)

myString = "hello"
myString1 = 'hellooo'
myString2 = "così posso scrivere con l'apostrofo"
myString3 = 'anche così posso scrivere con l\' apostrofo'

one = 1
two = 2
three = one + two

hello = "hello"
world = "world"
hw = hello + ' ' + world

print(hw)

numbers = []
strings = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

second_name = strings[1]

for x in strings:
    print(x)

for x in numbers:
    print(x)

print(int(10/4))
print(10.0/4)
print(10%2 == 11%2)