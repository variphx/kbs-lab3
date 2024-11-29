import json
from pathlib import PurePath
import schema
from knowledge import *


class InputsWithValue:
    def __init__(self, inner: dict[str, float]):
        self.inner = inner

    @staticmethod
    def from_json(path: PurePath):
        with open(path, "r") as f:
            data = json.load(f)

        inputs = data["input"]
        input_values = data["input_values"]

    def __getitem__(self, key: str):
        return self.inner.__getitem__(key)

    def __repr__(self):
        return self.inner.__repr__()

    def add(self, key: str, value: float):
        self.inner.update({key: value})

    def to_kwargs(self):
        return self.inner

    def to_inputs(self):
        return Inputs(self.inner.keys())


class Computer:
    def __init__(self, computation_path: list[dict[str, any]]):
        self.computation_path = computation_path

    def compute_from(self, input_with_values: InputsWithValue, output: Output):
        x = input_with_values
        for step in self.computation_path:
            function_parts = step["function_parts"]
            fn = schema
            for function_part in function_parts:
                fn = getattr(fn, function_part)

            output_value = fn(**x.to_kwargs())
            output = step["output"]

            x.add(output, output_value)

        return x[output]


class ProblemParser:
    def __init__(self, input_with_values: InputsWithValue, output: Output):
        self.input_with_values = input_with_values
        self.output = output

    @staticmethod
    def from_json(path: PurePath):
        with open(path, "r") as f:
            data = json.load(f)

        inputs = data["input"]
        input_values = data["input_values"]
        input_with_values = InputsWithValue(dict(zip(inputs, input_values)))
        output = Output(data["output"])
        return ProblemParser(input_with_values, output)
