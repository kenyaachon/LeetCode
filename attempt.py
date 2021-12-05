def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def parrot(voltage, state='a stiff', action='voom', type='Norwegian'):
    print("--This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it")
    print("--Lovely plumage, the", type)
    print("-- It's", state, "!")

def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

def prime():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
            else:
                print(n, 'is a primer number')


f100 = fib2(100)
print(f100)
parrot(voltage=10000, action='VOOOOM')

cheeseshop("Limburger", "It's very runnning, sir.",
"It's really very, VERY runny, sir.",
shopkeeper="Michael Palin",
client="John Cleese",
sketch="Cheese Shop Sketch")

prime()
    