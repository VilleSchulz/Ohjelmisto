import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C,color="yellow", linewidth = 3, linestyle= "-")
plt.plot(X,S,color="green", linewidth = 3, linestyle= "-")

plt.show()