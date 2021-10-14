#remember np.diag(np.hstack([1/sigma[:r],np.zeros(n-r)]))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

X, y, coefficients = make_regression(
    n_samples=50,
    n_features=3,
    n_targets=1,
    n_informative=1,
    noise=5,
    coef=True,
    random_state=46
)

#number of columns
n=X.shape[1]
# rank
r = np.linalg.matrix_rank(X)  #np.linalg is the linear algebra module

# we basically want w = X^pseudoinverse of Y
# X^pseudoinverse calls for SVD decomposition of # X
# SVD
U, sigma, VT = np.linalg.svd(X, full_matrices=False)

sigma_plus = np.diag(np.hstack([1/sigma[:r], np.zeros(n-r)]))

X_plus = (VT.T).dot(sigma_plus).dot(U.T)

w=X_plus.dot(y)
print("least squares solution - linear regression:", w)

error = np.linalg.norm(X.dot(w) - y, ord=2)**2
print("error least squares solution - linear regression:", error)
