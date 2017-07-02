import math
import statistics as stat
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import plotly as py
import csv


def get_probability(rand_nums, range_list):
    '''
    Gets probability of a value occurring given a set of random values and ranges
    :param rand_nums: List of random numbers
    :param range_list: List of different values of ranges
    :return: List of probabilities for a given range
    '''
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
num_bins = 18

ranges = [mu + value*sigma for value in range(-4, 5)]

# To gather values
g_rand = np.random.normal(mu, sigma, 5000)

fig = plt.figure()
n, bins, patches = plt.hist(g_rand, num_bins, normed=1, facecolor='red', alpha=0.6)
# best fit line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Probability')
plt.ylabel('Value')


with open('gauss_values.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i for i in range(-4, 5)])
    writer.writerow(ranges)
    writer.writerow([])
    writer.writerow(['-4 to -3', '-3 to -2', '-2 to -1', '-1 to 0', '0 to 1', '1 to 2', '2 to 3', '3 to 4'])
    writer.writerow(get_probability(g_rand, ranges))

plot_url = py.plotly.plot_mpl(fig, filename='histogram_gauss')