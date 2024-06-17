import matplotlib.pyplot as plt
import numpy as np

# Generate an array of x values
x = np.linspace(0, 2 * np.pi, 100)  # 0 to 2*pi with 1000 points

# Calculate the sine of each x value
y = np.sin(x)

# Create the plot with dots as markers
plt.plot(x, y, 'o')  # 'o' specifies dots as the marker

# Add title and labels
plt.title('Sine Wave')
plt.xlabel('x values (radians)')
plt.ylabel('sin(x)')

# Display the plot
plt.grid(True)
plt.show()