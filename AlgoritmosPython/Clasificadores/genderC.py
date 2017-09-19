#librerias or kind of
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

#decision tree es un arbol binario

# altura,peso,talla
X=[[181,70,44],[177,68,43],[170,57,38],[154,58,37],[166,63,40],[190,90,47],
    [173,61,39],[177,98,40],[158,55,37],[171,66,42],[181,95,43]]

Y=['male','male','female','female','male','male','female','male'
    ,'female','male','male']

testX = [[175,63,43],[180,69,44],[162,54,38]]
testY = ['male','male','female']

#classification tree
clf= tree.DecisionTreeClassifier()
clf= clf.fit(X,Y)

#classification GaussianNB
clf2 = GaussianNB()
clf2.fit(X,Y)

#classification neighbors
clf3 = KNeighborsClassifier(n_neighbors=3,algorithm='auto')
clf3.fit(X,Y)

#classification SVC
clf4 = SVC()
clf4.fit(X,Y)

alt = input("Ingresa tu altura: ")
peso = input("Ingresa tu peso: ")
talla = input("Ingresa tu talla de zapato: ")

predicition = clf.predict([[int(alt),int(peso),int(talla)]])
points = clf.score(testX,testY)
#190,70,43
print (predicition,"\n La precision de decision tree fue de:",points)

prediction = clf2.predict([[int(alt),int(peso),int(talla)]])
points = clf2.score(testX,testY)

print(prediction,"\n La precision de gaussianNB es de: ",points)

prediction = clf3.predict([[int(alt),int(peso),int(talla)]])
points = clf3.score(testX,testY)

print(prediction,"\n La precision de neighbors es de: ",points)

prediction = clf4.predict([[int(alt),int(peso),int(talla)]])
points = clf4.score(testX,testY)

print(prediction,"\n La precision de SVC es de: ",points)
