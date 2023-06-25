import pickle

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# import dataset
df = pd.read_csv('ShipCollisionDataset.csv')
print(df)

y = df["Collision"]
x = df.drop(['Collision'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

#Make pickle
pickle.dump(model, open("model.pkl", "wb"))

# print(x)