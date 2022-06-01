
import time


def fibRecu(n):
    if n < 2: return n
    return fibRecu(n-1) + fibRecu(n-2)


def fibYield(n):
    if n < 2: yield n
    yield fibRecu(n-1) + fibRecu(n-2)



def fibMemoRe(n):
    memo = {}
    def F(i):
        if i < 2: return i
        if i not in memo:
            memo[i] = F(i-1) + F(i-2)
        return memo[i]
    return F(n)

def fib(n):
    F = {}
    F[0], F[1] = 0, 1
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]



start = time.time()
print(fib(40))
print(f"time taken {time.time() - start}")
print("iterate solution bottom up")

start = time.time()
print(fibMemoRe(40))
print(f"time taken {time.time() - start}")
print("recursive solution bottom up")

start = time.time()
print(list(fibYield(40))[-1])
print(f"time taken {time.time() - start}")
print("yield solution")

start = time.time()
print(fibRecu(40))
print(f"time taken {time.time() - start}")
print("regular recursive solution ")
