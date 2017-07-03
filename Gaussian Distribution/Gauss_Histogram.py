import math
import statistics as stat
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import plotly as py
import csv


def get_probability(rand_nums, range_list):
    probabilities = []
    for index, val in enumerate(range_list[:len(range_list) - 1]):
        # List of probabilities for each range by summing total count in range and dividing by total count
        range_count = sum(1 for i in rand_nums if val <= i <= range_list[index + 1])
        probabilities.append(range_count/len(rand_nums))
    return probabilities

# Learn about API authentication here: https://plot.ly/python/getting-started
# API setup https://plot.ly/settings/api
py.tools.set_credentials_file(username='Username', api_key='APIKEY')

# Enter your Z-number here
z_num = 12345678
z_num_list = [int(i) for i in str(z_num)]

mean = stat.mean(z_num_list)
n = stat.median(z_num_list)
M = sum(z_num_list)
sigma = math.sqrt(M)
mu = mean
num_bins = 25

g_ranges = [mu + value*sigma for value in range(-4, 5)]

# To gather values
g_rand = np.random.normal(mu, sigma, size=5000)

gauss_fig = plt.figure()
g_array, g_bins, g_patches = plt.hist(g_rand, num_bins, normed=1, facecolor='red', alpha=0.6)
# best fit line
y = mlab.normpdf(g_bins, mu, sigma)
plt.plot(g_bins, y, 'r--')
plt.title('Gaussian Distribution')
plt.xlabel('Probability')
plt.ylabel('Value')

g_plot_url = py.plotly.plot_mpl(gauss_fig, filename='histogram_gauss_1')
plt.clf()

triangle_fig = plt.figure()
b = 2 * n
# Create triangular range
t_ranges = [(i * b)/4 for i in range(9)]
# Calculate standard deviation
t_sd = math.sqrt((b**2 + (2*b)**2 - b*(2*b))/18)

# Generate random values
t_rand = np.random.triangular(0, b, 2*b, size=5000)
t_array, t_bins, t_patches = plt.hist(t_rand, num_bins, normed=1, facecolor='blue', alpha=0.5)
x = mlab.normpdf(t_bins, b, t_sd)
plt.plot(t_bins, x, 'r--')
plt.title('Triangular Distribution')
plt.xlabel('Probability')
plt.ylabel('Value')
t_plot_url = py.plotly.plot_mpl(triangle_fig, filename='histogram_triangle_1')


with open('gauss_values_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i for i in range(-4, 5)])
    writer.writerow(g_ranges)
    writer.writerow(['Gaussian Distribution'])
    writer.writerow(['{:4f} to {:4f}'.format(value, g_ranges[index + 1])
                     for index, value in enumerate(g_ranges[:len(g_ranges) - 1])])
    writer.writerow(get_probability(g_rand, g_ranges))
    writer.writerow(['Triangular Distribution'])
    writer.writerow(['{} to {}'.format(value, t_ranges[index + 1])
                     for index, value in enumerate(t_ranges[:len(t_ranges) - 1])])
    writer.writerow(get_probability(t_rand, t_ranges))