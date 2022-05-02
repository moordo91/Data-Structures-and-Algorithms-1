global stkA, stkB, stkC
stkA = []; stkB = []; stkC = []

def printStack(stack):
    if stack == []:
        return "NULL"
    else:
        return ",".join(str(i) for i in reversed(stack))

def hanoi(n, start, temp, end):
    global stkA, stkB, stkC
    if n == 1:
        globals()['stk{}'.format(end)].append(globals()['stk{}'.format(start)].pop())
        print(
            'A', "(", printStack(stkA), ") \t",
            'B', "(", printStack(stkB), ") \t",
            'C', "(", printStack(stkC), ") ",
        )
    else:
        hanoi(n-1, start, end, temp)
        globals()['stk{}'.format(end)].append(globals()['stk{}'.format(start)].pop())
        print(
            'A', "(", printStack(stkA), ") \t",
            'B', "(", printStack(stkB), ") \t",
            'C', "(", printStack(stkC), ") ",
        )
        hanoi(n-1, temp, start, end)

n = int(input())
for i in range(5, 0, -1):
    stkA.append(i)
hanoi(n, 'A', 'B', 'C')

