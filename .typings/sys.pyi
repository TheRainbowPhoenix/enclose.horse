from typing import Callable, Final, Literal, NoReturn

class Implementation(tuple[str, tuple[int, int, int], int]):
    name: str
    version: tuple[int, int, int]
    mpy: int

class ModuleType:
    __class__: str
    __name__: str

argv: Final[list[str]] = ...
"""
A mutable list of arguments the current program was started with.
"""

byteorder: Final[Literal["little", "big"]] = ...
"""
The byte order of the system (``"little"`` or ``"big"``).
"""

def exit(retval: object = 0) -> NoReturn:
    """
   Terminate current program with a given exit code. Underlyingly, this
   function raise as `SystemExit` exception. If an argument is given, its
   value given as an argument to `SystemExit`.
   """

implementation: Final[Implementation] = ...
"""
Object with information about the current Python implementation. For
   MicroPython, it has following attributes:

   * *name* - string "micropython"
   * *version* - tuple (major, minor, micro), e.g. (1, 7, 0)

   This object is the recommended way to distinguish MicroPython from other
   Python implementations (note that it still may not exist in the very
   minimal ports).

   .. admonition:: Difference to CPython
      :class: attention

      CPython mandates more attributes for this object, but the actual useful
      bare minimum is implemented in MicroPython.
"""

modules: Final[dict[str, ModuleType]] = ...
"""
Dictionary of loaded modules. On some ports, it may not include builtin
   modules.
"""

path: Final[list[str]] = ...
"""
A mutable list of directories to search for imported modules.

   .. admonition:: Difference to CPython
      :class: attention

      On MicroPython, an entry with the value ``".frozen"`` will indicate that import
      should search :term:`frozen modules <frozen module>` at that point in the search.
      If no frozen module is found then search will *not* look for a directory called
      ``.frozen``, instead it will continue with the next entry in ``sys.path``.
"""

def print_exception(exc: BaseException, file: str = "stdout") -> None:
    """
   Print exception with a traceback to a file-like object *file* (or
   `sys.stdout` by default).
   
   .. admonition:: Difference to CPython
      :class: attention
   
      This is simplified version of a function which appears in the
      ``traceback`` module in CPython. Unlike ``traceback.print_exception()``,
      this function takes just exception value instead of exception type,
      exception value, and traceback object; *file* argument should be
      positional; further arguments are not supported. CPython-compatible
      ``traceback`` module can be found in `micropython-lib`.
   
   .. function:: settrace(tracefunc)
   
   Enable tracing of bytecode execution.  For details see the `CPython
   documentaion <https://docs.python.org/3/library/sys.html#sys.settrace>`_.
   
   This function requires a custom MicroPython build as it is typically not
   present in pre-built firmware (due to it affecting performance).  The relevant
   configuration option is *MICROPY_PY_SYS_SETTRACE*.
   """

version: Final[str] = ...
"""
Python language version that this implementation conforms to, as a string.
"""

version_info: Final[tuple[int, int, int]] = ...
"""
Python language version that this implementation conforms to, as a tuple of ints.

    .. admonition:: Difference to CPython
      :class: attention

      Only the first three version numbers (major, minor, micro) are supported and
      they can be referenced only by index, not by name.
"""