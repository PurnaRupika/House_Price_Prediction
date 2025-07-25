import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.datasets import fetch_openml

house=fetch_openml(name='house_prices',as_frame=True)
data=house.frame

data.head()

missing=data.isnull().mean()
drop_columns=missing[missing>0.2].index
data.drop(columns=drop_columns,inplace=True)

data.head()

data.dropna(inplace=True)
data=pd.get_dummies(data,drop_first=True)
X=data.drop('SalePrice',axis=1)
y=data['SalePrice']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

plt.figure(figsize=(8,6))
plt.scatter(y_test,y_pred,alpha=0.6,color='green')
plt.plot([y.min(),y.max()],[y.min(),y.max()],color='red',linestyle='--')
plt.xlabel("Actual Sale Price")
plt.ylabel("Predicted Sale Price")
plt.title("Actual vs Predicted House Prices")
plt.show()

