#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel="rbf", C = 10000.0)
#inicio = time()
clf.fit(features_train, labels_train)
#print("Fit demorou: ", time()-inicio)
#inicio = time()
pred = clf.predict(features_test)
#print("Pred demorou: ", time()-inicio)
#print(accuracy_score(pred, labels_test))
total = 0
for x in pred:
	total += x
print("A cris teve ", total, " emails e a Sara teve ", len(pred)-total, "emails")
#############################################
#print("Resultado posicao 10: ", pred[10])
#print("Resultado posicao 26: ", pred[26])
#print("Resultado posicao 50: ", pred[50])
#############################################
total = 0
for x in labels_test:
	total += x
print("A cris teve ", total, " emails e a Sara teve ", len(labels_test)-total, "emails")
print("End Program!")