import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class color_index_adder(BaseEstimator, TransformerMixin):
    def __init__(self, filters = ['u', 'g', 'r', 'i', 'z']):
        self.filters = filters
    
    def fit(self, X, y=None):
        return self  

    def transform(self, df, y=None):
        galaxy_filer = df['u'] - df['g'] 
        star_fiter = df['g'] - df['r']
        quasar_filter_1 = df['g'] - df['r']
        quasar_filer_2 = df['u'] - df['g'] 

        # Ensure the output is a 2D array
        return np.c_[df, galaxy_filer, star_fiter, quasar_filter_1, quasar_filer_2].reshape(-1, 1)