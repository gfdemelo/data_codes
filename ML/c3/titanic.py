#!/usr/bin/env python

import pandas as pd, numpy as np



#Lendo os dados
train_data = pd.read_csv('handson-ml2-master/datasets/titanic/train.csv')
test_data = pd.read_csv('handson-ml2-master/datasets/titanic/test.csv')

#Legendas
# Survived: that's the target, 0 means the passenger did not survive, while 1 means he/she survived.
# Pclass: passenger class.
# Name, Sex, Age: self-explanatory
# SibSp: how many siblings & spouses of the passenger aboard the Titanic.
# Parch: how many children & parents of the passenger aboard the Titanic.
# Ticket: ticket id
# Fare: price paid (in pounds)
# Cabin: passenger's cabin number
# Embarked: where the passenger embarked the Titanic. C=Cherbourg, Q=Queenstown, S=Southampton


#Análise dos Dados
train_data.head()
train_data.info()
test_data.head()
test_data.info()
train_data.info()
train_data.describe()
train_data['Survived'].value_counts()

#Construindo as pipelines para preencher valores e transformar

from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):
    """Seleciona atributos específicos dos dados"""
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names]

#Pipeline para atributos numéricos de interesse: Age, SibSp, Parch, Fare

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

num_pipeline = Pipeline([
        ("select_numeric", DataFrameSelector(["Age", "SibSp", "Parch", "Fare"])),
        ("imputer", SimpleImputer(strategy="median")),
    ])

num_pipeline.fit_transform(train_data)

#Transformando dados não-numéricos
class MostFrequentImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.most_frequent_ = pd.Series([X[c].value_counts().index[0] for c in X],
                                        index=X.columns)
        return self
    def transform(self, X, y=None):
        return X.fillna(self.most_frequent_)

#Pipeline dos atributos categoricos
from sklearn.preprocessing import OneHotEncoder
cat_pipeline = Pipeline([
        ("select_cat", DataFrameSelector(["Pclass", "Sex", "Embarked"])),
        ("imputer", MostFrequentImputer()),
        ("cat_encoder", OneHotEncoder(sparse=False)),
    ])

cat_pipeline.fit_transform(train_data)

#Unindo os pipelines numericos e categoricos

from sklearn.pipeline import FeatureUnion
preprocess_pipeline = FeatureUnion(transformer_list=[
        ("num_pipeline", num_pipeline),
        ("cat_pipeline", cat_pipeline),
    ])

X_train = preprocess_pipeline.fit_transform(train_data)

#Labels
y_train = train_data["Survived"]

#Treinando um classifier, fazendo previsões e cross-validation

from sklearn.svm import SVC

svm_clf = SVC(gamma="auto")
svm_clf.fit(X_train, y_train)

X_test = preprocess_pipeline.transform(test_data)
y_pred = svm_clf.predict(X_test)

from sklearn.model_selection import cross_val_score

svm_scores = cross_val_score(svm_clf, X_train, y_train, cv=10)
print(svm_scores.mean())

#Usando outro classifier

from sklearn.ensemble import RandomForestClassifier

forest_clf = RandomForestClassifier(n_estimators=100, random_state=42)
forest_scores = cross_val_score(forest_clf, X_train, y_train, cv=10)
print(forest_scores.mean())


