import pickle
import matplotlib.pyplot as plt
import numpy as np 
from cutecharts.charts import Bar, Line

with open("rates", "rb") as fp: 
    rate = pickle.load(fp)
index = np.linspace(1, len(rate), len(rate))
index = index.tolist()


chart = Line("Review")
chart.set_options(labels=index , x_label="review", y_label="rate")
chart.add_series("stars", rate)
chart.render()

# plt.bar(index, rate, width = 0.5)
# # plt.plot(index, rate, "g" , marker = 'D' , markersize = 5 )
# plt.show()
