from stack import Stack

my_stack = Stack()

print(f'Stack top = {my_stack.top()}')
print(f'Stack size = {my_stack.size()}')
print(f'If stack is empty = {my_stack.empty()}')

my_stack.push("Jonathan")
my_stack.push("Joshua")
my_stack.push("Daniel")
my_stack.push("Luis")
my_stack.push("Fabian")
my_stack.push("Kevin")
my_stack.push("Gustavo")
my_stack.push("Derek")
my_stack.push("Alex")
my_stack.push("David")
my_stack.push("Isaac")

print(f'Stack top = {my_stack.top()}')
print(f'Stack size = {my_stack.size()}')
print(f'If stack is empty = {my_stack.empty()}')

print('\nStack elements\n')

for student in my_stack.iter():
    print(student)

print('\nPop and element\n')
print(my_stack.pop())

print('\nStack elements\n')

for student in my_stack.iter():
    print(student)