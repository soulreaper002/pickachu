import numpy as np
import matplotlib.pyplot as plt
 # f\left(x\right)=\left(\sqrt[3]{x}\right)^{2}+\ \frac{e}{3}\cdot\sqrt{\left(\pi-x^{2}\right)}\cdot\sin\left(a\pi x\right)
a = 16.7
x = np.linspace(-np.sqrt(np.pi), np.sqrt(np.pi), 1000)
x_pow = np.cbrt(x)**2
y = x_pow + (np.e / 3) * np.sqrt(np.pi - x**2) * np.sin(a * np.pi * x)

plt.figure(figsize=(8, 6)) 
plt.plot(x, y, 'r')
plt.title(f'a = {a}')
plt.grid(True)
plt.axis('equal')
plt.show()