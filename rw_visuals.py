import matplotlib.pyplot as plt
import random

def random_walk(n_steps):
    """Generate a random walk with n_steps."""
    x_values = [0]
    y_values = [0]
    
    for _ in range(n_steps):
        x_step = random.choice([-1, 0, 1])
        y_step = random.choice([-1, 0, 1])
        
        if x_step == 0 and y_step == 0:
            continue
        
        x_values.append(x_values[-1] + x_step)
        y_values.append(y_values[-1] + y_step)
    
    return x_values, y_values

# Generate a random walk with 5000 steps
x_values, y_values = random_walk(5000)

# Plot the random walk
#plt.figure(figsize=(10, 6))
point_numbers = list(range(len(x_values)))
fig,ax = plt.subplots()
ax.plot(x_values, y_values)
plt.title('2D Random Walk')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()
