import math
import statistics as stat
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import plotly as py
import csv

# Learn about API authentication here: https://plot.ly/python/getting-started
# API setup https://plot.ly/settings/api
py.tools.set_credentials_file(username='kbman', api_key='99cUPeQHHIoTSGZ97oRb')

# Enter your Z-number here
z_num = 23313497
z_num_list = [int(i) for i in str(z_num)]

mean = stat.mean(z_num_list)
n = stat.median(z_num_list)
M = sum(z_num_list)
sigma = math.sqrt(M)
mu = mean
num_bins = 18

ranges = [mu + value*sigma for value in range(-4, 5)]

# To gather values
with open('gauss_values.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([i for i in range(-4, 5)])
    writer.writerow(ranges)

g_rand = np.random.normal(mu, sigma, 5000)

fig = plt.figure()
n, bins, patches = plt.hist(g_rand, num_bins, normed=1, facecolor='red', alpha=0.6)
# best fit line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Probability')
plt.ylabel('Value')

plot_url = py.plotly.plot_mpl(fig, filename='histogram_gauss')

