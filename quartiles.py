from data import data

# This line imports the statistics module for your convenience. You don't need to modify this.
import statistics as st
quartiles = st.quantiles(data)
q3 = quartiles[2]
q1 = quartiles[0]
iqr = quartiles[2] - quartiles[0]
print('quartiles', quartiles)
print('q3', q3)
print('q1', q1)
print('iqr',iqr)
