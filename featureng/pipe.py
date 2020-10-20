
import numpy as np

from . import transform
from . import scale
from . import interaction

from .PipelineStep import PipelineStep

class FeatureTransform(PipelineStep):
    def __init__(self,indexmap:dict={}):
        self.indexmap = indexmap

    def predict(self,X,y,*):
        X2 = X.copy()
        for col, fn in self.indexmap.items():
            X2[col] = fn(X2[col])
        return X2

# class MinMaxScaler(PipelineStep):
#     def _get_extent(self,data):
#         self.extent = np.min(X), np.max(X)
#         return self.extent

#     def _scale(self,data):
#         min_, max_ = self.extent
#         return (data - min_) / (max_ - min_)

#     def fit(self,X,y,*):
#         self._get_extent(X)
#         return self._scale(X)

#     def predict(self,X,*):
#         return self._scale(X)

# class Standardizer(PipelineStep):
#     def _get_params(self,data):
#         self._mean = np.mean(data)
#         self._std = np.std(data)

#     def _transform(self,data):
#         return (data - self._mean) / self._std

#     def fit(self,X,y,*):
#         self._get_params(X)
#         return self._transform(X)

#     def predict(self,X,*):
#         return self._transform(X)

# class L2Normalizer(PipelineStep):
#     def _get_params(self,data):
#         self._mean = np.mean(data)
#         self._std = np.std(data)

#     def _transform(self,data):
#         return (data - self._mean) / self._std

#     def fit(self,X,y,*):
#         self._get_params(X)
#         return self._transform(X)

#     def predict(self,X,*):
#         return self._transform(X)  
