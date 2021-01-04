### Dictionaries


data = dict(a=3, c=4, b=1) # Keys müssen unique sein
data = [("a", 3), ("c", 4), ("b", 1)]
data = {"a": 3, "c": 4, "b": 1}

data = {"a": 4, "c": 4, "b": 1}
data = {"a": 1, "a": 2}

#https://stackoverflow.com/questions/8169001/why-is-bool-a-subclass-of-int#:~:text=It%20kind%20of%20makes%20sense,storage%20space)....

data
data = {True: 1, 1: 3, 1.0: 2}

d = {}
d[True] = 1
d[1.0] = 3

d
True == 1 == 1.0

issubclass(bool, int)
isinstance(True, int)


data
#data = dict([1,2,3]=3, c=4, b=1) # keys müssen hashable sein

data
hash([1,2,3])

"a".__len__()
"a".__hash__()

sorted(data.values())

data.keys()
data.items()
data.values()

sorted(data.items(), key=lambda x:x[1])

data.popitem()
data.pop("x", "not found")
data.update(b=3)
data.clear()
data

