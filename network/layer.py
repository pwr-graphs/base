from pylog import *

from .models import ModelBase


class Layer:
    def __init__(self, model, **params):
        if not isinstance(model, ModelBase):
            err('Model is not instance of ModelBase class')

        self._model = model
        self._params = params

    def __call__(self):
        return self._model.gen(**self._params)

    def __str__(self):
        return self.name

    @property
    def model(self):
        return self._model.gen

    @property
    def params(self):
        return self._params

    @property
    def name(self):
        return self._model.name
