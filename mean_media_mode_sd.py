# DO NOT MODIFY THE FOLLOWING LINE. It sets up the data that you'll need for this exercise.
from data import data

# This line imports the statistics module for your convenience. You don't need to modify this.
import statistics as st

list_mean = st.mean(data)
list_mode = st.mode(data)
list_median = st.median(data)
list_std = st.stdev(data)
print('Mean: ', list_mean)
print('Median:', list_median)
print('Mode: ', list_mode)
print('STD: ', list_std)
