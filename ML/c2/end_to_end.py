#!/usr/bin/env python

import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit



housing = pd.read_csv('../handson-ml2-master/datasets/housing/housing.csv')
#housing.hist(bins=50, figsize=(20,15))
#plt.show()

#################CRIANDO UM TESTE#########################

def split_train_test(data, test_ratio):
	shuffled_indices = np.random.permutation(len(data))
	test_set_size = int(len(data * test_ratio))
	test_indices = shuffled_indices[:test_set_size]
	train_indices = shuffled_indices[test_set_size:]
	return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42) #faz o mesmo que split_train_test
#print(train_set[:10])
housing['income_cat'] = pd.cut(housing['median_income'], bins=[0.,1.5,3.0,4.5,6.,np.inf], labels=[1,2,3,4,5])
#housing['income_cat'].hist()
#plt.show()

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
	strat_train_set = housing.loc[train_index]
	strat_test_set = housing.loc[test_index]

#comparação entre conjuntos estratificados, total e random

print(strat_test_set['income_cat'].value_counts() / len(strat_test_set))
print(housing['income_cat'].value_counts() / len(housing))
test_set['income_cat'] = pd.cut(test_set['median_income'],  bins=[0.,1.5,3.0,4.5,6.,np.inf], labels=[1,2,3,4,5])
print(test_set['income_cat'].value_counts() / len(test_set))

for set_ in (strat_train_set, strat_test_set):
	set_.drop('income_cat', axis=1, inplace=True)

################VISUALIZANDO E DESCOBRINDO DADOS################

casa = strat_train_set.copy()
casa.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4, s=casa['population']/100, label='population', figsize=(10,7), c='median_house_value', cmap=plt.get_cmap('jet'), colorbar=True)
#plt.show()

#Correlação entre dados
from pandas.plotting import scatter_matrix

corr_matrix = casa.corr()
print(corr_matrix['median_house_value'].sort_values(ascending=False))
attributes = ['median_house_value', 'median_income', 'total_rooms', 'housing_median_age']
scatter_matrix(casa[attributes], figsize=(12,8))
plt.show()

#Experimentando novos atributos
casa['rooms_per_household'] = casa['total_rooms'] / casa['households']
casa['bedrooms_per_room'] = casa['total_bedrooms'] / casa['total_rooms']
casa['population_per_household'] = casa['population'] / casa['households']
corr_matrix2 = casa.corr()
print(corr_matrix2['median_house_value'].sort_values(ascending=False))

####################PREPARANDO OS DADOS##############################

copia = strat_train_set.drop('median_house_value', axis=1)
copia_labels = strat_train_set['median_house_value'].copy()

#limpando os dados e substituindo faltantes

from sklearn.impute import SimpleImputer          #para substituir dados faltantes em "bedrooms"pela mediana
imputer = SimpleImputer(strategy='median')
copia_num = copia.drop('ocean_proximity', axis=1)
imputer.fit(copia_num)
#print(imputer.statistics_)

X = imputer.transform(copia_num)
copia_tr = pd.DataFrame(X, columns=copia_num.columns, index=copia_num.index)

#Handling categorias com textos

copia_cat = copia[['ocean_proximity']]
#print(copia_cat.head(10))

from sklearn.preprocessing import OrdinalEncoder          #categoriza em numeros os possivels "ocean Proximity"
ordinal_encoder = OrdinalEncoder()
copia_cat_encoded = ordinal_encoder.fit_transform(copia_cat)
#print(ordinal_encoder.categories_)

from sklearn.preprocessing import OneHotEncoder           #Cria um atributo binário por categoria
cat_encoder = OneHotEncoder()
copia_cat_1hot = cat_encoder.fit_transform(copia_cat)
copia_cat_1hot = copia_cat_1hot.toarray()


#Transformação customizada

from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self 
    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

num_pipeline = Pipeline([('imputer', SimpleImputer(strategy='median')), ('attribs_adder', CombinedAttributesAdder()), ('std_scaler', StandardScaler())])
copia_num_tr = num_pipeline.fit_transform(copia_num)

from sklearn.compose import ColumnTransformer
num_attribs = list(copia_num)
cat_attribs = ['ocean_proximity']
full_pipeline = ColumnTransformer([ ('num', num_pipeline, num_attribs), ('cat', OneHotEncoder(), cat_attribs)])
copia_prepared = full_pipeline.fit_transform(copia)



######################SELECIONANDO E TREINANDO O MODELO ########################

from sklearn.linear_model import LinearRegression

#Usando Regressão Linear

lin_reg = LinearRegression()
lin_reg.fit(copia_prepared, copia_labels)

some_data = housing.iloc[:5]
some_data = copia.iloc[:5]
some_labels = copia_labels[:5]
some_data_prepared = full_pipeline.transform(some_data)
print('Predictions:', lin_reg.predict(some_data_prepared))
print('Labels:', list(some_labels))   		#Erro grande

#Verificando RMSE do modelo de Regressao Linear

from sklearn.metrics import mean_squared_error
copia_predictions = lin_reg.predict(copia_prepared)
lin_mse = mean_squared_error(copia_labels, copia_predictions)
lin_rmse = np.sqrt(lin_mse)


#Usando o modelo DecisionTreeRegressor

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()
tree_reg.fit(copia_prepared, copia_labels)
copia_predictions = tree_reg.predict(copia_prepared)
tree_mse = mean_squared_error(copia_labels, copia_predictions)
tree_rmse = np.sqrt(tree_mse)
print('RMSE DecisionTreeRegressor:', tree_rmse)			#Deu erro zero. Mas está correto?

#Cross-Validation do DecisionTreeRegressor

from sklearn.model_selection import cross_val_score

scores = cross_val_score(tree_reg, copia_prepared, copia_labels, scoring='neg_mean_squared_error', cv=10)
tree_rmse_scores = np.sqrt(-scores)

def display_scores(scores):
    print('Scores:', scores)
    print('Mean:', scores.mean())
    print('Standard Deviation:', scores.std())
print(display_scores(tree_rmse_scores))				#Erro pior que regressao Linear

#Cross-Validation do Linear Regression para comparação

lin_scores = cross_val_score(lin_reg, copia_prepared, copia_labels, scoring='neg_mean_squared_error', cv=10)
lin_rmse_scores = np.sqrt(-lin_scores)
print(display_scores(lin_rmse_scores))

#Usando o modelo RandomForestRregressor

from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor()
forest_reg.fit(copia_prepared, copia_labels)

copia_predictions = forest_reg.predict(copia_prepared)
forest_mse = mean_squared_error(copia_labels, copia_predictions)
forest_rmse = np.sqrt(forest_mse)
forest_scores = cross_val_score(forest_reg, copia_prepared, copia_labels, scoring='neg_mean_squared_error', cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)
print(display_scores(forest_rmse_scores))			#Melhor resultado



######################### LAPIDANDO O MELHOR MODELO ####################

from sklearn.model_selection import GridSearchCV

forest_reg = RandomForestRegressor()
param_grid = [{'n_estimators':[3,10,30], 'max_features':[2,4,6,8]},{'bootstrap':[False],'n_estimators':[3,10], 'max_features':[2,3,4]}]
grid_search = GridSearchCV(forest_reg, param_grid, cv=5, scoring='neg_mean_squared_error', return_train_score=True)
grid_search.fit(copia_prepared, copia_labels)

print(grid_search.best_params_)
print(grid_search.best_estimator_)
cvres = grid_search.cv_results_

for mean_score, params in zip(cvres['mean_test_score'], cvres['params']):
    print(np.sqrt(-mean_score), params)					#Menor Valor é o melhor hyperparameter


######################## AVALIAR O MODELO FINAL NO TEST SET ####################

final_model = grid_search.best_estimator_
X_test = strat_test_set.drop('median_house_value', axis=1)
y_test = strat_test_set['median_house_value'].copy()
X_test_prepared = full_pipeline.transform(X_test)

final_predictions = final_model.predict(X_test_prepared)
final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)


#Computando o intervalo de 95% de confiança
from scipy import stats
confidence = 0.95
squared_errors = (final_predictions - y_test) ** 2
print(np.sqrt(stats.t.interval(confidence, len(squared_errors) - 1, loc=squared_errors.mean(), scale=stats.sem(squared_errors))))

