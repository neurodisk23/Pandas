import pandas as pd
import matplotlib.pyplot as plt


# Create a figure and axes
fig, ax = plt.subplots()

# Plot the first dataframe
ax.plot(df['p_lat_'], df['p_lon'], label='PixHawk')

# Plot the second dataframe
ax.plot(df['n_lat'], df['n_lon'], label='Novatel')

# Set labels and title
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_title('Overlapping GPS Coordinates Graphs')

# Add a legend
ax.legend()

# Display the plot
plt.show()
