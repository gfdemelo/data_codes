#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



dados_heart = pd.read_csv('heart.csv')
print(dados_heart.head())
print(dados_heart.describe())
print(dados_heart.info())
print(dados_heart.isnull().any())
print(dados_heart['output'].agg(['count', 'size', 'nunique']))
print(pd.value_counts(dados_heart['output']))

#Plotagem

fig = plt.figure()
ax = fig.add_subplot(111)
print(dados_heart['age'].value_counts())
a = dados_heart['age'].value_counts()
a = a.sort_values()
a.plot(kind='bar', title='Age to Count Plot', x='Age', y='Count', cmap=plt.get_cmap('jet'), figsize=(10,5))
plt.legend()
plt.show()

#Correlação entre os dados

corr_matrix = dados_heart.corr()
print(corr_matrix['output'].sort_values(ascending=False))
chest_pain_count = dados_heart['cp'].value_counts().reset_index()
print(chest_pain_count)

#Standardizing Independent Variables

from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(dados_heart, dados_heart['cp']):
    strat_train_set = dados_heart.loc[train_index]
    strat_test_set = dados_heart.loc[test_index]

X_train = strat_train_set.iloc[:, 0:-1].values
y_train = strat_train_set.iloc[:, -1].values

X_test = strat_test_set.iloc[:, 0:-1].values
y_test = strat_test_set.iloc[:, -1].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

#Montando o modelo para testar

accuracy_scores = {}
def predictor(predictor, params):
    global accuracy_scores
    if predictor == 'lr':
        print('Training Logistic Regression on Training Set')
        from sklearn.linear_model import LogisticRegression
        classifier = LogisticRegression(**params)

    elif predictor == 'svm':
        print('Training Support Vector Machine on Training Set')
        from sklearn.svm import SVC
        classifier = SVC(**params)

    elif predictor == 'knn':
        print('TrainingK-Nearest Neighbours on Training Set')
        from sklearn.neighbors import KNeighborsClassifier
        classifier = KNeighborsClassifier(**params)

    elif predictor == 'dt':
        print('Training LDecision Tree Classifier on Training Set')
        from sklearn.tree import DecisionTreeClassifier
        classifier = DecisionTreeClassifier(**params)

    elif predictor == 'nb':
        print('Training Naive Bayes Classifier on Training Set')
        from sklearn.naive_bayes import GaussianNB
        classifier = GaussianNB(**params)

    elif predictor == 'rfc':
        print('Training Random Forest Classifier on Training Set')
        from sklearn.ensemble import RandomForestClassifier
        classifier = RandomForestClassifier(**params)

    elif predictor == 'linreg':
        print('Linear Regression')
        from sklearn.linear_model import LinearRegression
        classifier = LinearRegression(**params)

    elif predictor == 'treereg':
        print('Decision Tree Regressor')
        from sklearn.tree import DecisionTreeRegressor
        classifier = DecisionTreeRegressor(**params)


    classifier.fit(X_train, y_train)

    print('''Predicting Single Cell Result''')
    single_predict = classifier.predict(sc.transform([[
        63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1
    ]]))
    if single_predict > 0.5:
        print("Heart Attack\n")
    else:
        print("No Heart Attack \n")

    print('''Prediciting Test Set Result''')
    y_pred = classifier.predict(X_test)
    result = np.concatenate((y_pred.reshape(len(y_pred), 1),
                             y_test.reshape(len(y_test), 1)), 1)
    print(result, '\n')
    print('''Making Confusion Matrix''')
    from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, np.round(y_pred))
    print(cm, '\n')
    print('True Positives :', cm[0][0])
    print('False Positives :', cm[0][1])
    print('False Negatives :', cm[1][0])
    print('True Negatives :', cm[0][1], '\n')

    print('''Classification Report''')
    print(classification_report(y_test, np.round(y_pred),
          target_names=['M', 'B'], zero_division=1))

    print('''Evaluating Model Performance''')
    accuracy = accuracy_score(y_test, np.round(y_pred))
    print(accuracy, '\n')

    #Cross-Validation
    print('''Applying K-Fold Cross validation''')
    from sklearn.model_selection import cross_val_score
    accuracies = cross_val_score(
        estimator=classifier, X=X_train, y=y_train, cv=10)
    print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
    accuracy_scores[classifier] = accuracies.mean()*100
    print("Standard Deviation: {:.2f} %".format(accuracies.std()*100), '\n')


#Training Logistic Regression on Training Set
predictor('lr', {'penalty': 'l1', 'solver': 'liblinear'})
#Training SVM on Training Set
predictor('svm', {'C': .5, 'gamma': 0.8,'kernel': 'linear', 'random_state': 0})
#Training Kernel SVM on Training Set
predictor('svm', {'C': .25, 'gamma': 0.1, 'kernel': 'rbf', 'random_state': 0})
#Training K-Nearest Neighbours on Training Set
predictor('knn', {'algorithm': 'auto', 'n_jobs': 1,'n_neighbors': 6, 'weights': 'uniform'})
#Training Decision Tree on Training Set
predictor('dt', {'criterion': 'entropy', 'max_features': 'auto','splitter': 'best', 'random_state': 0})
#Training Naive Bayes on Training Set
predictor('nb', {})
#Training Random Forest Classifier on Training Set
predictor('rfc', {'criterion': 'gini','max_features': 'log2', 'n_estimators': 500,'random_state': 0})
#Linear Regression
predictor('linreg', {})
#Decision Tree
predictor('treereg',{})


#Finding the best performance
maxKey = max(accuracy_scores, key=lambda x: accuracy_scores[x])
print('The model with highest K-Fold Validation Accuracy score is  {0} with an accuracy of  {1:.2f}'.format(
    maxKey, accuracy_scores[maxKey]))

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
model_accuracies = list(accuracy_scores.values())
model_names = ['LogisticRegression', 'SVC',
               'K-SVC', 'KNN', 'Decisiontree', 'GaussianNB', 'RandomForest', 'Linear Regression', 'DecisionTreeRegressor']

ax.barh(y=model_names, width=model_accuracies)
plt.show()

