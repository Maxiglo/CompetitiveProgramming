def f(x):
    return x**2+2*x+3

def ff(t):
    return f(f(f(t)+t)+f(f(t)))

n = int(input())
print(ff(n))