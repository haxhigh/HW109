import pandas as pd
import csv 
import statistics as st
import plotly.figure_factory as ff

df = pd.read_csv("C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw/Hw109/StudentsPerformance.csv")
file = df["math score"].tolist()

mean = sum(file) / len(file)
mode = st.mode(file)
median = st.median(file)
dev = st.stdev(file)

print("The Standard Deviasion is:" + str(dev))
print("The mean is: " + str(mean))
print("The mode is: " + str(mode))
print("The median is: " + str(median))

fig = ff.create_distplot([file],["Math Results"])
fig.show()