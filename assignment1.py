"""
UK Rainfall Visualization
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FixedLocator


def line_plot(x, y):
    """
    Create a line plot of yearly rainfall in the UK.

    Args:
        x (list): List of years.
        y (list): List of annual rainfall values.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))

    years = x
    rainfall = y

    plt.plot(years, rainfall, label='Annual Rainfall', color='b')

    plt.title('Yearly Rainfall in the UK (1836-2023)')
    plt.xlabel('Year')
    plt.ylabel('Rainfall (mm)')
    plt.legend(loc='upper left')
    plt.grid(True)

    # Set major x-ticks every 10 years and minor x-ticks every 1 year
    major_locator = MultipleLocator(10)
    minor_locator = FixedLocator(years)
    ax = plt.gca()
    ax.xaxis.set_major_locator(major_locator)
    ax.xaxis.set_minor_locator(minor_locator)
    plt.xticks(rotation=45)
    plt.xlim(years.min(), years.max())
    plt.show()


def area_plot(data):
    """
    Create an area plot of seasonal rainfall in the UK.

    Args:
        data (DataFrame): DataFrame containing seasonal rainfall data.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    plt.stackplot(
        data['year'],
        data['win'],
        data['spr'],
        data['sum'],
        data['aut'],
        labels=[
            'Winter',
            'Spring',
            'Summer',
            'Autumn'],
        alpha=0.7)

    plt.title('Seasonal Rainfall in the UK')
    plt.xlabel('Year')
    plt.ylabel('Rainfall (mm)')
    # Set major x-ticks every 10 years and minor x-ticks every 1 year
    plt.legend(loc='upper left')
    major_locator = MultipleLocator(10)
    minor_locator = FixedLocator(data['year'])
    ax = plt.gca()
    ax.xaxis.set_major_locator(major_locator)
    ax.xaxis.set_minor_locator(minor_locator)
    plt.xticks(rotation=45)
    plt.xlim(data['year'].min(), data['year'].max())
    plt.grid(True)

    plt.show()


def bar_plot(data):
    """
    Create a bar plot of monthly rainfall for every decades from 1940 to 2020 in the UK.

    Args:
        data (DataFrame): DataFrame containing monthly rainfall data.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
              '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#b29c58', '#f0027f']

    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]

    # Downsample the data to show every 10 years
    downsampled_data = data[data['year'] % 10 == 0]

    # Loop through each year and create bars for each month
    for i, row in downsampled_data.iterrows():
        x = row['year']
        y = [row[month] for month in months]
        plt.bar(x, y, color=colors, alpha=0.7, width=6)

    # Create a custom legend with distinct colors for the months
    legend_labels = [plt.Line2D([0], [0], color=color, lw=4, label=month)
                     for color, month in zip(colors, months)]
    plt.legend(handles=legend_labels, loc='upper left', ncol=2)

    x_ticks = downsampled_data['year'].tolist()
    plt.xticks(x_ticks, rotation=45)

    plt.title('Monthly Rainfall in the UK (Every 10 Years)')
    plt.xlabel('Year')
    plt.ylabel('Rainfall (mm)')

    plt.show()


# Read dataset
data_file = 'data.csv'
data = pd.read_csv(data_file)

# Line plot
line_plot(data.year, data.ann)

# Area Plot
area_plot(data)

# Bar plot
bar_plot(data)
