"""
___By ~ Captain Thunder___
---------------------------------
Gives different gradient in each opening
---------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
import random

#random colormap
all_colormaps = plt.colormaps()
random_colormap = random.choice(all_colormaps)

# Parametric equations for heart shape
t = np.linspace(0, 2 * np.pi, 1000)
x_base = 16 * np.sin(t)**3
y_base = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plotting
plt.figure(figsize=(8, 8), facecolor='#000')
scaling_factors = np.linspace(0.1, 3, 15)[::-1]
colors = plt.colormaps[random_colormap](np.linspace(0, 1, len(scaling_factors)))
for factor, color in zip(scaling_factors, colors):
    x = x_base * factor
    y = y_base * factor
    plt.plot(x, y, color=color, alpha=0.3)
    plt.fill(x, y, color=color, alpha=1)
plt.gca().set_facecolor('#fff')
plt.title(f'PyHeart ({random_colormap})', color='#fff', fontsize = 40)
plt.grid(False)
plt.savefig('j.png')
plt.show()
