from sklearn.base import BaseEstimator, TransformerMixin

class ColorIndicesAdder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self  

    def transform(self, X, y=None):
        X['galaxy_filter'] = X['u'] - X['g']
        X['star_filter'] = X['g'] - X['r']
        X['quasar_filter_1'] = X['g'] - X['r']
        X['quasar_filter_2'] = X['u'] - X['g']
        return X
    
class ToDataFrame(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.DataFrame(X, columns=self.columns)