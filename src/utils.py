import matplotlib.pyplot as plt

def plot(time_points, states, n_row):
    first_column = [sublist[n_row] for sublist in states]
    plt.plot(time_points, first_column)
    plt.savefig('1.png')


plot([0,1,2,3],[[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]],0)

def plot(time_points, states, n_row, save_path='plot.png', title=None, xlabel='Time', ylabel='State', grid=True):
    """
    Plots a specific row from a 2D array against time points and saves the figure.
    
    Parameters:
    - time_points (list): X-axis values (e.g., time steps).
    - states (list of lists): 2D array where each sublist represents a state.
    - n_row (int): Row index to plot (0 for first row, 1 for second, etc.).
    - save_path (str): File path to save the plot (default: 'plot.png').
    - title (str): Plot title (optional).
    - xlabel (str): X-axis label (default: 'Time').
    - ylabel (str): Y-axis label (default: 'State').
    - grid (bool): Whether to show grid lines (default: True).
    """
    if n_row >= len(states[0]):
        raise ValueError(f"n_row={n_row} is out of bounds (max={len(states[0])-1})")
    
    selected_row = [sublist[n_row] for sublist in states]
    
    plt.figure(figsize=(8, 5))  # Adjust figure size
    plt.plot(time_points, selected_row, marker='o', linestyle='-', color='b', label=f'Row {n_row}')
    
    if title:
        plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(grid)
    
    plt.tight_layout()  # Prevent label cutoff
    plt.savefig(save_path)
    plt.close()  # Close the figure to free memory

# Example usage
plot(
    time_points=[0, 1, 2, 3],
    states=[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]],
    n_row=0,
    save_path='row_plot.png',
    title='First Row vs Time',
    xlabel='Time (s)',
    ylabel='State Value'
)