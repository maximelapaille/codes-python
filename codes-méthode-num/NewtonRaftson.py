from numpy import *
from matplotlib import pyplot as plt

f = lambda x :sin(x)
dfdx = lambda x : cos(x)

def NewR (X0,tol,nmax) : 
    n = 0 
    x = X0
    x_vals = [X0]
    delta = float("inf")
    while abs(delta)>tol and n <nmax :
        delta = f(x)/dfdx(x)
        x = x - delta
        n += 1
        x_vals.append(x)

    return x, x_vals

print(NewR(3 , 0.00001 , 1000))
print(pi)

sol, trace = NewR(3 , 0.00001 , 1000)

x_vals = linspace(-10, 10, 4000)

plt.plot(x_vals, f(x_vals), label='f(x)')
plt.axhline(0, color='black', linestyle='--')
plt.plot(trace, [f(x) for x in trace], 'ro-', label='Itérations NR')
plt.title("Méthode de Newton-Raphson")
plt.xlabel("x"); plt.ylabel("f(x)")
plt.grid(True); plt.legend()
plt.show()
