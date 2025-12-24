import numpy as np
import matplotlib.pyplot as plt


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

x = np.arange(0,10,0.1)

y = np.sin(x)

plt.plot(x,y,'-', label='sin(x)')
plt.plot(0,0)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.tight_layout()
plt.savefig('sinx.png',dpi=300)
plt.show()