from typing import Any, BinaryIO, Iterable, List, Literal, Tuple, TypeVar, Union

_T = TypeVar('_T')

class array:
    """
   |see_cpython_module| :mod:`python:array`.
   
   Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
   ``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
   floating-point support).
   
    +-----------+--------------------+-------------------+-----------------------+
    | Type code | C Type             | Python Type       | Minimum size in bytes |
    +===========+====================+===================+=======================+
    | ``'b'``   | signed char        | int               | 1                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'B'``   | unsigned char      | int               | 1                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'h'``   | signed short       | int               | 2                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'H'``   | unsigned short     | int               | 2                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'i'``   | signed int         | int               | 2                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'I'``   | unsigned int       | int               | 2                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'l'``   | signed long        | int               | 4                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'L'``   | unsigned long      | int               | 4                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'q'``   | signed long long   | int               | 8                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'Q'``   | unsigned long long | int               | 8                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'f'``   | float              | float             | 4                     |
    +-----------+--------------------+-------------------+-----------------------+
    | ``'d'``   | double             | float             | 8                     |
    +-----------+--------------------+-------------------+-----------------------+
   """

    def __init__(
        self,
        typecode: Literal[
            'b', 'B', 'u', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd', 'O', 'P', 'S'
        ],
        initializer: Union[bytes, bytearray, Iterable[int], Iterable[float]] = [],
    ) -> None:
        """
        Create array with elements restricted by typecode.
        
        Type codes:
        - 'b': signed byte (1 byte)
        - 'B': unsigned byte (1 byte)
        - 'u': Unicode char (2 bytes)
        - 'h': signed short (2 bytes)
        - 'H': unsigned short (2 bytes)
        - 'i': signed int (2 bytes)
        - 'I': unsigned int (2 bytes) 
        - 'l': signed long (4 bytes)
        - 'L': unsigned long (4 bytes)
        - 'q': signed long long (8 bytes)
        - 'Q': unsigned long long (8 bytes)
        - 'f': float (4 bytes)
        - 'd': double (8 bytes)
        - 'O': Python objects
        - 'P': pointers
        - 'S': strings (deprecated)
        
        Example:
        ```
        a = array.array('I', [0]*10)  # Unsigned int array
        b = array.array('f', [1.5, 2.5])  # Float array
        ```
        """
        ...
    
    def append(self, x: Union[int, float, Any]) -> None:
        """Append item to end of array."""
        ...
    
    def buffer_info(self) -> Tuple[int, int]:
        """
        Return (address, length) of memory buffer.
        
        Example:
        ```py
        addr, length = arr.buffer_info()
        ```
        """
        ...
    
    def byteswap(self) -> None:
        """Swap bytes of all items (endianness conversion)."""
        ...
    
    def count(self, x: Any) -> int:
        """Return number of occurrences of x."""
        ...
    
    def extend(self, iterable: Iterable[Union[int, float, Any]]) -> None:
        """Append items from iterable."""
        ...
    
    def fromfile(self, f: BinaryIO, n: int) -> None:
        """Read n items from file object and append them."""
        ...
    
    def fromlist(self, list: List[Union[int, float, Any]]) -> None:
        """Append items from list."""
        ...
    
    def frombytes(self, s: bytes) -> None:
        """Append items from bytes string."""
        ...
    
    def index(self, x: Any) -> int:
        """Return index of first occurrence of x."""
        ...
    
    def insert(self, i: int, x: Union[int, float, Any]) -> None:
        """Insert item at position i."""
        ...
    
    def pop(self, i: int = -1) -> Union[int, float, Any]:
        """Remove and return item at index i (default last)."""
        ...
    
    def remove(self, x: Any) -> None:
        """Remove first occurrence of x."""
        ...
    
    def reverse(self) -> None:
        """Reverse order of items in-place."""
        ...
    
    def tofile(self, f: BinaryIO) -> None:
        """Write all items to file object."""
        ...
    
    def tolist(self) -> List[Union[int, float, Any]]:
        """Convert array to list."""
        ...
    
    def tobytes(self) -> bytes:
        """Convert array to bytes string."""
        ...
    
    def __len__(self) -> int: ...
    def __getitem__(self, i: int) -> Union[int, float, Any]: ...
    def __setitem__(self, i: int, x: Union[int, float, Any]) -> None: ...
    def __iter__(self) -> Iterable[Union[int, float, Any]]: ...
    def __contains__(self, x: Any) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...