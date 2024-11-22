from collections import deque
def reverse(stack, stacktoadd):
    while stack:
        popped = stack.pop()
        stacktoadd.append(popped)
stack = deque()
stacktoadd = deque()
palavras = input()
palavras = palavras.split(" ")
for i in range(len(palavras)):
    stack.append(palavras[i])
reverse(stack,stacktoadd)
print(stacktoadd)
while stacktoadd:
    popped = stacktoadd.pop()
    if "a" in popped:
        print(popped)