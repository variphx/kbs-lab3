import typing
import json
import itertools
from pathlib import PurePath


class Inputs:
    def __init__(self, inner: typing.Iterable[str]):
        self.inner = set(inner)
        self.__sorted_inner = tuple(sorted(self.inner))

    def sorted(self):
        return self.__sorted_inner

    def add(self, element: str):
        self.inner.add(element)
        self.__sorted_inner = tuple(sorted(self.inner))

    def __hash__(self):
        return self.__sorted_inner.__hash__()

    def __eq__(self, value: typing.Self):
        return self.inner.__eq__(value.inner)

    def __contains__(self, value: typing.Self):
        return self.inner.__contains__(value)

    def __iter__(self):
        return self.inner.__iter__()

    def __str__(self):
        return self.inner.__str__()

    def __repr__(self):
        return self.inner.__repr__()


class Output(str):
    pass


class FunctionParts:
    def __init__(self, inner: typing.Iterable[str]):
        self.inner = list(inner)

    def __len__(self):
        return self.inner.__len__()

    def __iter__(self):
        return self.inner.__iter__()

    def __str__(self):
        return self.inner.__str__()

    def __repr__(self):
        return self.inner.__repr__()


class KnowledgeNetwork:
    def __init__(self, inner: dict[Inputs, dict[str, any]]):
        self.inner = inner

    def __getitem__(self, key: Inputs):
        return self.inner.__getitem__(key)

    def __str__(self):
        return self.inner.__str__()

    def __repr__(self):
        return self.inner.__repr__()

    @staticmethod
    def from_json(path: PurePath):
        f = open(path, "r")
        data: typing.Iterable[dict] = json.load(f)
        f.close()

        inner = dict(map(KnowledgeNetwork.__from_json_helper, data))
        return KnowledgeNetwork(inner)

    @staticmethod
    def __from_json_helper(data: dict[str, any]):
        inputs = Inputs(data["input"])
        output = Output(data["output"])
        function_parts = FunctionParts(data["function"])
        return inputs, {"output": output, "function_parts": function_parts}
