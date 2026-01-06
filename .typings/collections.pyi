from typing import overload, Any, Type, Iterable, TypeVar, Generic, Mapping, Dict, Final

_KT: Final = TypeVar("_KT")
_VT: Final = TypeVar("_VT")

def namedtuple(name: str, fields: str | Iterable[str]) -> Type[tuple[Any, ...]]:
    """
    This is factory function to create a new namedtuple type with a specific
    name and set of fields. A namedtuple is a subclass of tuple which allows
    to access its fields not just by numeric index, but also with an attribute
    access syntax using symbolic field names. Fields is a sequence of strings
    specifying field names. For compatibility with CPython it can also be a
    a string with space-separated field named (but this is less efficient).

    Example:
    ```
    from collections import namedtuple

    MyTuple = namedtuple("MyTuple", ("id", "name"))
    t1 = MyTuple(1, "foo")
    t2 = MyTuple(2, "bar")
    print(t1.name)
    assert t2.name == t2[1]

    Point = namedtuple('Point', ['x', 'y'])

    # instantiate with positional args or keywords
    p = Point(11, y=22)

    # indexable like a plain tuple
    p[0] + p[1]  # 33

    # unpack like a regular tuple
    x, y = p 
    x, y  # (11, 22)

    # fields also accessible by name
    p.x + p.y  # 33
    ```
    """
    ...

        