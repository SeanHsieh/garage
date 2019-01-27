"""This file contains the abstraction class for models."""
from garage.tf.models import AutoPickable


class BaseModel:
    """Abstraction class for models."""

    def build_model(self):
        """
        Build model.

        This function will build the whole graph for
        the model. All tensors should be created here.
        By calling this function, a copy of the same graph
        should be created with the same parameters.
        """
        raise NotImplementedError

    @property
    def input(self):
        """Tensor input of the Model."""
        if len(self.model.inputs) == 1:
            return self.model.inputs[0]

        return self.model.inputs

    @property
    def output(self):
        """Tensor output of the Model."""
        if len(self.model.outputs) == 1:
            return self.model.outputs[0]

        return self.model.outputs

    @property
    def inputs(self):
        """Tensor inputs of the Model."""
        return self.model.inputs

    @property
    def outputs(self):
        """Tensor outputs of the Model."""
        return self.model.outputs


class PickableModel(AutoPickable):
    """Abstraction class for autopickable models."""

    def build_model(self):
        """
        Build model.

        This function will build the whole graph for
        the model. All tensors should be created here.
        By calling this function, a copy of the same graph
        should be created with the same parameters.
        """
        raise NotImplementedError

    @property
    def input(self):
        """Tensor input of the Model."""
        if len(self.model.inputs) == 1:
            return self.model.inputs[0]

        return self.model.inputs

    @property
    def output(self):
        """Tensor output of the Model."""
        if len(self.model.outputs) == 1:
            return self.model.outputs[0]

        return self.model.outputs

    @property
    def inputs(self):
        """Tensor inputs of the Model."""
        return self.model.inputs

    @property
    def outputs(self):
        """Tensor outputs of the Model."""
        return self.model.outputs
