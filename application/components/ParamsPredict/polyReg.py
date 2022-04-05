import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#pruebas 
dir0= '../../assets/'
dir = './application/assets'
#df = pd.read_csv("../../assets/data/values1.csv")
df = pd.read_csv(f"{dir}/data/values2.csv")

X = df.a.values.reshape(-1,1)
y = df.lc.values.reshape(-1,1)

def lambdaValue(alpha):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    
    lin_reg = LinearRegression()
    lin_reg.fit(X, y)

    # Fitting Polynomial Regression 
    poly_reg = PolynomialFeatures(degree=11)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)

    # Predicting a new result Polymonial Regression
    pred = pol_reg.predict(poly_reg.fit_transform([[alpha]]))
    pred = int(pred[0][0])

    return pred