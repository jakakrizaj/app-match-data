import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import random

trees_per_ha = random.randint(350, 500)
x_bound = [-20, 20]
y_bound = [-20, 20]
plot_size = ((max(x_bound) - min(x_bound)) * (max(y_bound) - min(y_bound))) / 10000
trees_on_plot = int(trees_per_ha * plot_size)
x_shift = random.randint(-20, 20)
y_shift = random.randint(-15, 15)
rotation = np.radians(random.randint(-180, 180))

id_ref = np.array(range(0, trees_on_plot))
x_ref = np.round((np.random.randint(x_bound[0], x_bound[1], trees_on_plot) + np.random.sample(trees_on_plot)), 2)
y_ref = np.round((np.random.randint(y_bound[0], y_bound[1], trees_on_plot) + + np.random.sample(trees_on_plot)), 2)
dbh_ref = np.round((np.random.normal(40, 20, trees_on_plot) + np.random.sample(trees_on_plot)), 2)
df_ref = pd.DataFrame({"id_ref" : id_ref,
                       "x_ref" : x_ref,
                       "y_ref" : y_ref,
                       "dbh_ref" : dbh_ref})
df_ref = df_ref.loc[df_ref["dbh_ref"] > 10]

x_las = (np.cos(rotation) * x_ref - np.sin(rotation) * y_ref) + x_shift #cosx - siny
y_las = (np.sin(rotation) * x_ref + np.sin(rotation) * y_ref) + y_shift #sinx + cosy
dbh_las = []
for dbh in dbh_ref:
    if np.random.random() < 0.5:
        new_dbh = dbh - np.random.normal(dbh, 2, 1)
        dbh_las.append(new_dbh)
    else:
        new_dbh = dbh + np.random.normal(dbh, 2, 1)
        dbh_las.append(new_dbh)


print(trees_on_plot)
print(df_ref)

plt.scatter(df_ref["x_ref"], df_ref["y_ref"], s=df_ref["dbh_ref"])
plt.show()