# 4.11
my_pizza = ['pizza hut', 'pizza burg', 'dominos', 'pizza burger']
my_fpizza = my_pizza[:]

print('here are my pizza list: ')
print(my_pizza)
print()

print('here are my friends pizza list: ')
print(my_fpizza)
print()

my_pizza.append('pizza bug')
my_fpizza.append('pizza king')

print('here are the new different list of my pizza: ')
print(my_pizza)
print()

print('here are the new different list of friend pizza: ')
print(my_fpizza)
print()

print('new list: ')
for pizza in my_pizza:
    print(pizza)
print()

for pizza in my_fpizza:
    print(pizza)
print()
