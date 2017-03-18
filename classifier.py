import pandas as pd

#Load data.csv
df=pd.read_csv('data.csv', sep=',',header=None, names=['Genre', 'Artist', 'Title', 'UniqueLinesRatio'])
X, y = df.iloc[1:,3:], df.iloc[1:, 1]

print(X)
print(y)

#Classify
from sklearn.neighbors.nearest_centroid import NearestCentroid

clf = NearestCentroid()
clf.fit(X, y)
NearestCentroid(metric='euclidean', shrink_threshold=None)
print(clf.predict([[1]]))
