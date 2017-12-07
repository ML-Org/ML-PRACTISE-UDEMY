import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Dataset/Data.csv")
X = dataset.iloc[: , : -1].values;
Y = dataset.iloc[: , 3].values;
print(X);
print(Y);

# taking care of missing data - taking mean of other observations

from sklearn.preprocessing import Imputer
# axs =0 -> column wide
#axs = 1 -> row wide
imputer = Imputer(missing_values='NaN',strategy="mean",axis=0)
imputer.axis(X);



