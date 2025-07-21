import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import sys
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Donut parameters
R = 2  # Major radius
r = 1  # Minor radius

# Create meshgrid for angles
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Donut parametric equations
def get_donut(R, r, theta, phi, rot=0):
    # Accept scalar or array theta/phi
    x = (R + r * np.cos(theta)) * np.cos(phi + rot)
    y = (R + r * np.cos(theta)) * np.sin(phi + rot)
    z = r * np.sin(theta)
    return x, y, z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Ensure ax is an Axes3D instance
if not isinstance(ax, Axes3D):
    ax = Axes3D(fig)
ax.set_box_aspect([1,1,1])

def animate(i):
    ax.clear()
    x, y, z = get_donut(R, r, theta, phi, rot=i * 0.05)
    ax.plot_surface(x, y, z, cmap='plasma', edgecolor='none')
    ax.set_xlim(-R-r, R+r)
    ax.set_ylim(-R-r, R+r)
    ax.set_zlim(-r, r)
    ax.set_axis_off()
    ax.set_title("3D Moving Donut")

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
# Instead of plt.show(), render ASCII donut in terminal using symbols for shading


# ASCII shades from dark to light
shades = ".,-~:;=!*#$@"
def render_ascii_donut(frame):
    output = []
    for j in range(40):
        row = ""
        for i in range(80):
            # Map i, j to angles
            theta = 2 * np.pi * i / 80
            phi = 2 * np.pi * j / 40
            x, y, z = get_donut(R, r, theta, phi, rot=frame * 0.05)
            # z is scalar, so shade_idx is valid
            shade_idx = int((z + r) / (2 * r) * (len(shades) - 1))
            shade_idx = max(0, min(shade_idx, len(shades) - 1))  # Clamp index
            row += shades[shade_idx]
        output.append(row)
    sys.stdout.write("\x1b[H")  # Move cursor to top
    print("\n".join(output))
    print("\n".join(output))


# Clear screen
print("\x1b[2J")
for frame in range(100):
    render_ascii_donut(frame)
    time.sleep(0.05)