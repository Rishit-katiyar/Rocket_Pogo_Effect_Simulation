

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.widgets import Button, TextBox
import matplotlib.gridspec as gridspec

# Initialize parameters with default values
default_params = {
    'm': 1000,      # Mass of the rocket (kg)
    'k': 5000,      # Spring constant (N/m)
    'c': 200,       # Damping coefficient (Ns/m)
    'F': 20000,     # Thrust force (N)
    'dt': 0.01,     # Time step (s)
    't_max': 10,    # Maximum simulation time (s)
    'rocket_width': 1.0,  # Width of the rocket (m)
    'rocket_height': 4.0  # Height of the rocket (m)
}
params = default_params.copy()
x, v = 0.0, 0.0   # Initial displacement and velocity

# Create figure and axis
fig = plt.figure(figsize=(14, 10))
gs = gridspec.GridSpec(3, 3, height_ratios=[0.05, 0.5, 0.5])
ax = plt.subplot(gs[1:, :2])
control_ax = plt.subplot(gs[0, 0])
status_ax = plt.subplot(gs[2, 0])
text_ax = plt.subplot(gs[0, 1])
button_ax = plt.subplot(gs[2, 1])
info_ax = plt.subplot(gs[:, 2])

ax.set_xlim(0, params['rocket_width'])
ax.set_ylim(0, 10)  # Assuming display height is 10m

# Initialize rocket
rocket = Polygon([(0, 0), (params['rocket_width'], 0), (params['rocket_width'], params['rocket_height']), (0, params['rocket_height'])], closed=True, color='blue')
fuel_label = ax.text(0.5 * params['rocket_width'], 0.5 * params['rocket_height'], 'Fuel', ha='center', va='center', color='white', fontsize=12)
ax.add_patch(rocket)

# Function to update rocket position
def update(frame):
    global x, v, rocket, fuel_label
    a = (params['F'] - params['k'] * x - params['c'] * v) / params['m']
    v += a * params['dt']
    x += v * params['dt']
    
    # Reflect motion at edges
    if x < 0:
        x = -x
        v = -v
    elif x + params['rocket_height'] > 10:  # Assuming display height is 10m
        x = 10 - params['rocket_height'] - (x + params['rocket_height'] - 10)
        v = -v
    
    rocket.set_xy([(0, x), (params['rocket_width'], x), (params['rocket_width'], x + params['rocket_height']), (0, x + params['rocket_height'])])
    fuel_label.set_position((0.5 * params['rocket_width'], x + 0.5 * params['rocket_height']))
    
    # Update graphs
    time_points.append(frame * params['dt'])
    displacement_points.append(x)
    velocity_points.append(v)
    acceleration_points.append(a)
    update_graphs()
    
    return [rocket, fuel_label]

# Initialize graphs
time_points = []
displacement_points = []
velocity_points = []
acceleration_points = []

time_line, = info_ax.plot([], [], label='Time (s)', color='blue')
displacement_line, = info_ax.plot([], [], label='Displacement (m)', color='green')
velocity_line, = info_ax.plot([], [], label='Velocity (m/s)', color='orange')
acceleration_line, = info_ax.plot([], [], label='Acceleration (m/s²)', color='red')
info_ax.legend(loc='upper right')
info_ax.set_xlabel('Time (s)')
info_ax.set_ylabel('Values')
info_ax.set_title('Rocket Dynamics')

# Function to update graphs
def update_graphs():
    time_line.set_data(time_points, displacement_points)
    displacement_line.set_data(time_points, displacement_points)
    velocity_line.set_data(time_points, velocity_points)
    acceleration_line.set_data(time_points, acceleration_points)
    info_ax.relim()
    info_ax.autoscale_view()
    fig.canvas.draw()

# Function to reset rocket
def reset_rocket():
    global rocket, fuel_label, x, v
    x, v = 0.0, 0.0
    ax.patches.clear()
    ax.texts.clear()
    rocket = Polygon([(0, 0), (params['rocket_width'], 0), (params['rocket_width'], params['rocket_height']), (0, params['rocket_height'])], closed=True, color='blue')
    fuel_label = ax.text(0.5 * params['rocket_width'], 0.5 * params['rocket_height'], 'Fuel', ha='center', va='center', color='white', fontsize=12)
    ax.add_patch(rocket)

# Function to update simulation parameters
def update_parameters():
    param_text = param_textbox.text
    param_list = param_text.split(',')
    try:
        for param in param_list:
            key, value = param.split('=')
            key = key.strip()
            value = float(value.strip())
            if key in params:
                params[key] = value
        reset_rocket()
    except ValueError as e:
        print(f"Error parsing parameters: {e}")

# Function to save animation
def save_animation(event):
    writer = PillowWriter(fps=24)
    ani.save('rocket_animation.gif', writer=writer, dpi=100)
    status_ax.clear()
    status_ax.text(0.5, 0.5, "Animation saved as 'rocket_animation.gif'.", ha='center', va='center', fontsize=12)
    status_ax.axis('off')
    plt.draw()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, params['t_max'], params['dt']), blit=True, interval=10)

# Control UI
param_textbox = TextBox(text_ax, 'Parameters (key=value, ...):', initial="m=1000, k=5000, c=200, F=20000, dt=0.01, t_max=10")
update_button = Button(button_ax, 'Update Parameters')
update_button.on_clicked(lambda event: update_parameters())

save_button = Button(control_ax, 'Save Animation')
save_button.on_clicked(save_animation)

plt.title('Rocket Pogo Effect Simulation')
ax.set_xlabel('Width (m)')
ax.set_ylabel('Height (m)')
ax.set_aspect('equal', adjustable='box')
ax.grid(True)
fig.tight_layout()

plt.show()
