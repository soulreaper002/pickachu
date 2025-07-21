import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo
 
# Parameters
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)
 
# 3D Heart Parametric Equations
x = 16 * np.sin(u)**3 * np.sin(v)
y = (13*np.cos(u) - 5*np.cos(2*u) - 2*np.cos(3*u) - np.cos(4*u)) * np.sin(v)
z = (13*np.cos(u) - 5*np.cos(2*u) - 2*np.cos(3*u) - np.cos(4*u)) * np.cos(v)
 
# Create Plotly surface plot
surface = go.Surface(x=x, y=y, z=z, colorscale='Reds')
 
layout = go.Layout(
    title='3D Heart Surface (Interactive)', scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    )
)
 
fig = go.Figure(data=[surface], layout=layout)
 
# Save to HTML file
pyo.plot(fig, filename='3d_heart.html')