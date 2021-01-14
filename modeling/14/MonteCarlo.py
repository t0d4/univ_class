import matplotlib.pyplot as plt
import numpy as np

N = input("Input N: ")
if not N:
    N = 100
else:
    N = int(N)

x = np.random.randint(1, 11, (N, ))
y = np.random.randint(1, 11, (N, ))
norms = np.linalg.norm((x, y), axis=0)
is_included = (norms <= 10)
x_included = x[is_included]
y_included = y[is_included]
x_excluded = x[np.logical_not(is_included)]
y_excluded = y[np.logical_not(is_included)]

estimated_pi = 4 * np.sum(is_included) / N

plt.axes().set_aspect('equal')
plt.xlim(0, 10)
plt.ylim(0, 10)

# plot random coordinates
plt.scatter(x_included, y_included, c="blue")
plt.scatter(x_excluded, y_excluded, c="red")

# display a circle
theta = np.linspace(0, np.pi/2)
plt.plot(10 * np.cos(theta), 10 * np.sin(theta))

plt.text(8, 9, f"N={N}")
plt.text(8, 8.5, f"pi={round(estimated_pi, 4)}")

plt.tight_layout()
plt.show()
