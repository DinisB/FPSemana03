from collections import deque
stack = deque()
palavras = input()
palavras = palavras.split(" ")
for i in range(len(palavras)):
    stack.appendleft(palavras[i])
print(stack)
while stack:
    popped = stack.pop()
    if "a" in popped:
        print(popped)