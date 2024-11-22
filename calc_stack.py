from collections import deque
numeros = input()
numeros = numeros.split(" ")
stack = deque()
for i in range(len(numeros)):
    stack.append(int(numeros[i]))
print(stack)
while stack:
    popped = stack.pop()
    print(popped * 2)