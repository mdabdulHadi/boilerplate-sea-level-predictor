import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.figure(figsize=(10, 6))
  plt.scatter(df['Year'],
              df['CSIRO Adjusted Sea Level'],
              label='Sea Level Data')

  # Create first line of best fit
  slope, intercept, _, _, _ = linregress(df['Year'],
                                         df['CSIRO Adjusted Sea Level'])
  years = range(1880, 2051)
  plt.plot(years,
           intercept + slope * years,
           'r',
           label='Best Fit Line (1880-2050)')

  # Create second line of best fit (from year 2000 to the most recent year)
  recent_df = df[df['Year'] >= 2000]
  slope_recent, intercept_recent, _, _, _ = linregress(
    recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
  plt.plot(years,
           intercept_recent + slope_recent * years,
           'g',
           label='Best Fit Line (2000-2050)')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  plt.legend()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()


# Call the function to generate the plot
draw_plot()
