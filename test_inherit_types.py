import timeit
from collections import UserDict
from collections.abc import MutableMapping

EPOCHS = 1_000_000
NUMBER = 10

class OwnDict(dict): pass

class OwnUserDict(UserDict): pass

class OwnMutableDict(MutableMapping):
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

def test_dict(build_include=False):
    global d
    if build_include: d = OwnDict()
    for i in range(EPOCHS): d[i] = i
    for i in range(EPOCHS): _ = d[i]

def test_userdict(build_include=False):
    global d
    if build_include: d = OwnUserDict()
    for i in range(EPOCHS): d[i] = i
    for i in range(EPOCHS): _ = d[i]

def test_mutablemapping(build_include=False):
    global d
    if build_include: d = OwnMutableDict()
    for i in range(EPOCHS): d[i] = i
    for i in range(EPOCHS): _ = d[i]

print(f"EPOCHS: {EPOCHS:_}".replace(",", "_"))
print(f"NUMBER: {NUMBER}\n==================")

d = OwnDict()
print("dict:", timeit.timeit(test_dict, number=NUMBER))
print("dict(Build_Include):", timeit.timeit(lambda:test_dict(build_include=True), number=NUMBER))

d = OwnUserDict()
print("UserDict:", timeit.timeit(test_userdict, number=NUMBER))
print("UserDict(Build_Include):", timeit.timeit(lambda:test_userdict(build_include=True), number=NUMBER))

d = OwnMutableDict()
print("MutableMapping:", timeit.timeit(test_mutablemapping, number=NUMBER))
print("MutableMapping(Build_Include):", timeit.timeit(lambda:test_mutablemapping(build_include=True), number=NUMBER))