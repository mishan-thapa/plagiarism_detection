import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

cell_df = pd.read_csv('final.csv')

feature_df = cell_df[['bigram_similarity','simword_similarity' , 'fingerprint_similarity','lsa_sim']]

#independent variables
x= np.asarray(feature_df)

#dependent variables 
y= np.asarray(cell_df['label'])

sc_X = StandardScaler()
x = sc_X.fit_transform(x)

from sklearn import svm

#SVC = support vector classifer
classifier = svm.SVC(kernel='linear', gamma = 'auto', C = 1)

#fitting the model 
classifier.fit(x,y)

#predicting label using 4 feature
y_pred = classifier.predict([[0.7,0.4,0.5,0.6]])