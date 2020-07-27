from sklearn import svm
"""
There are three different implementations of Support Vector Regression: 
SVR, NuSVR and LinearSVR. LinearSVR provides a faster implementation 
than SVR but only considers the linear kernel, while NuSVR implements a 
slightly different formulation than SVR and LinearSVR. 
"""
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X,y)
z = regr.predict([[1, 1]])
print(z)
print(type(z))

