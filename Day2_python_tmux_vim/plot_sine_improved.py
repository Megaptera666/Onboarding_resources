import matplotlib.pyplot as plt
import numpy as np
from time import sleep

def calculate_sine(x_start, x_end, num_points, amplitude, frequency):
    """
    Calculate sine values.

    Parameters:
    x_start (float): Start of x range.
    x_end (float): End of x range.
    num_points (int): Number of points.
    amplitude (float): Amplitude of the sine wave.
    frequency (float): Frequency of the sine wave.

    Returns:
    tuple: Arrays of x values and sine values.
    """
    x = np.linspace(x_start, x_end, num_points)
    y = amplitude * np.sin(frequency * x)
    return x, y

def plot_sine(x, y):
    """
    Plot the sine wave.

    Parameters:
    x (numpy array): X values.
    y (numpy array): Sine values.
    """
    # Create the plot with dots as markers
    plt.plot(x, y, 'o')  # 'o' specifies dots as the marker

    # Add title and labels
    plt.title('Sine Wave')
    plt.xlabel('x values (radians)')
    plt.ylabel('sin(x)')

    # Display the plot
    plt.grid(True)
    plt.show()

def print_sine_wave(y_values, amplitude, height):
    """
    Print the sine wave to the terminal.

    Parameters:
    y_values (list): Y values of the sine wave.
    amplitude (float): Amplitude of the sine wave.
    height (int): Height of the display.
    """
    for y in y_values:
        # Map the y value to a position in the height of the display
        scaled_y = int((y + amplitude) * (height - 1) / (2 * amplitude))
        # Create the line with a '*' at the position of the sine wave
        line = [' '] * height
        line[scaled_y] = '*'
        print(''.join(line))
        sleep(0.01)



if __name__ == "__main__":
    x_start = 0
    x_end = 2 * np.pi
    num_points = 100
    amplitude = 1.0
    frequency = 1.0

    x, y = calculate_sine(x_start, x_end, num_points, amplitude, frequency)
    plot_sine(x, y)

    # visualize the sine wave in terminal
    print_sine_wave(y, amplitude, 100)
    print("Completed")


