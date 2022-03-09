from queue import Queue
from structure import Structure

my_queue = Queue()

print(f'Queue top = {my_queue.front()}')
print(f'Queue size = {my_queue.size()}')
print(f'If queue is empty = {my_queue.empty()}')

my_queue.push_back("Jonathan")
my_queue.push_back("Joshua")
my_queue.push_back("Daniel")
my_queue.push_back("Luis")
my_queue.push_back("Fabian")
my_queue.push_back("Kevin")
my_queue.push_back("Gustavo")
my_queue.push_back("Derek")
my_queue.push_back("Alex")
my_queue.push_back("David")
my_queue.push_back("Isaac")

print(f'Queue top = {my_queue.front()}')
print(f'Queue size = {my_queue.size()}')
print(f'If queue is empty = {my_queue.empty()}')

print('\nQueue elements\n')

for student in my_queue.iter():
    print(student)

print('\nQueue elements\n')

for student in my_queue.iter():
    print(student)

print('\nPop an element\n')
print(my_queue.pop())

print('\nQueue elements\n')

for student in my_queue.iter():
    print(student)