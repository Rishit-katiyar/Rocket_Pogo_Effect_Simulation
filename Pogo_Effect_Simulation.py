





import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation, PillowWriter

# Function to update rocket position
def update(frame):
    global x, v, rocket, rocket_width, rocket_height, fuel_label
    a = (F - k * x - c * v) / m
    v += a * dt
    x += v * dt
    
    # Reflect motion at edges
    if x < 0:
        x = -x
        v = -v
    elif x + rocket_height > 10:  # Assuming display height is 10m
        x = 10 - rocket_height - (x + rocket_height - 10)
        v = -v
    
    rocket.set_xy([(0, x), (rocket_width, x), (rocket_width, x + rocket_height), (0, x + rocket_height)])
    fuel_label.set_position((0.5 * rocket_width, x + 0.5 * rocket_height))
    return [rocket, fuel_label]

# Function to initialize rocket
def initialize_rocket():
    global rocket, rocket_width, rocket_height, fuel_label
    rocket = Polygon([(0, 0), (rocket_width, 0), (rocket_width, rocket_height), (0, rocket_height)], closed=True, color='blue')
    fuel_label = ax.text(0.5 * rocket_width, 0.5 * rocket_height, 'Fuel', ha='center', va='center', color='white', fontsize=12)
    ax.add_patch(rocket)

# Function to update simulation parameters
def update_parameters():
    global m, k, c, F, dt, t_max
    print("Enter the following parameters (press Enter to keep current value):")
    m = float(input("Mass of the rocket (kg) [Default: 1000]: ") or m)
    k = float(input("Spring constant (N/m) [Default: 5000]: ") or k)
    c = float(input("Damping coefficient (Ns/m) [Default: 200]: ") or c)
    F = float(input("Thrust force (N) [Default: 20000]: ") or F)
    dt = float(input("Time step (s) [Default: 0.01]: ") or dt)
    t_max = float(input("Maximum simulation time (s) [Default: 10]: ") or t_max)

# Function to save animation
def save_animation():
    writer = PillowWriter(fps=24)
    ani.save('rocket_animation.gif', writer=writer, dpi=100)
    print("Animation saved as 'rocket_animation.gif'.")

# Initialize parameters with default values
m = 1000  # Mass of the rocket (kg)
k = 5000  # Spring constant (N/m)
c = 200   # Damping coefficient (Ns/m)
F = 20000 # Thrust force (N)
dt = 0.01 # Time step (s)
t_max = 10 # Maximum simulation time (s)
x = 0.0   # Initial displacement
v = 0.0   # Initial velocity
rocket_width = 1.0   # Width of the rocket (m)
rocket_height = 4.0  # Height of the rocket (m)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, rocket_width)
ax.set_ylim(0, 10)  # Assuming display height is 10m

# Initialize rocket
initialize_rocket()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, t_max, dt), blit=True, interval=10)

# Menu
while True:
    print("\nMenu:")
    print("1. Update parameters")
    print("2. Save animation")
    print("3. Show the default simulation (recommended)")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        update_parameters()
        initialize_rocket()  # Re-initialize rocket with updated parameters
    elif choice == "2":
        save_animation()
    elif choice == "3":
        break
    elif choice == "4":
        print("Exiting...")
        plt.close()
        break
    else:
        print("Invalid choice. Please enter again.")

plt.title('Rocket Pogo Effect Simulation')
plt.xlabel('Width (m)')
plt.ylabel('Height (m)')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.tight_layout()
plt.show()
