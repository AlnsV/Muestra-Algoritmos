#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
##plt.show()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

#K-NEARESTS NEIGHBORS

clf=KNeighborsClassifier(n_neighbors=8)
clf.fit(features_train,labels_train)
print(accuracy_score(clf.predict(features_test),labels_test),"K-nearest Neighbors")

#ADABOOST
clf1=AdaBoostClassifier(n_estimators=50,learning_rate=1)
clf1.fit(features_train,labels_train)
print(accuracy_score(clf1.predict(features_test),labels_test),"AdaBoost")

#RANDOM FOREST
clf2=RandomForestClassifier(n_estimators=20,min_samples_split=40)
clf2.fit(features_train,labels_train)
print(accuracy_score(clf2.predict(features_test),labels_test),"Random Forest")



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

try:
    prettyPicture(clf1, features_test, labels_test)
except NameError:
    pass

try:
    prettyPicture(clf2, features_test, labels_test)
except NameError:
    pass
