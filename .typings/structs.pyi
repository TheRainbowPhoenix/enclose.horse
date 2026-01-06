from typing import Any, Tuple, Union, Protocol

class ReadableBuffer(Protocol):
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> int: ...

class WriteableBuffer(ReadableBuffer, Protocol):
    def __setitem__(self, index: int, value: int) -> None: ...

def calcsize(fmt: Union[str, bytes]) -> int:
    """
    Return size in bytes of the struct described by the format string.
    
    Format characters:
    - 'b': signed byte (1)
    - 'B': unsigned byte (1)
    - 'h': short (2)
    - 'H': unsigned short (2)
    - 'i': int (4)
    - 'I': unsigned int (4)
    - 'l': long (4)
    - 'L': unsigned long (4)
    - 'q': long long (8)
    - 'Q': unsigned long long (8)
    - 'f': float (4)
    - 'd': double (8)
    - 's': char[] (length)
    - '?': bool (1)
    
    Example:
    ```py
    size = struct.calcsize('I f')  # Returns 8 (4 + 4)
    ```
    """
    ...

def pack(fmt: Union[str, bytes], *values: Any) -> bytes:
    """
    Pack values into bytes according to format string.
    
    Example:
    ```py
    data = struct.pack('I f', 42, 3.14)  # b'*\x00\x00\x00\xc3\xf5H@'
    ```
    """
    ...

def pack_into(fmt: Union[str, bytes], buffer: WriteableBuffer, offset: int, *values: Any) -> None:
    """
    Pack values into buffer at offset according to format.
    
    Example:
    ```py
    buf = bytearray(8)
    struct.pack_into('I f', buf, 0, 42, 3.14)
    ```
    """
    ...

def unpack(fmt: Union[str, bytes], buffer: ReadableBuffer) -> Tuple[Any, ...]:
    """
    Unpack bytes into tuple of values according to format.
    
    Example:
    ```py
    values = struct.unpack('I f', b'*\x00\x00\x00\xc3\xf5H@')
    # (42, 3.140000104904175)
    ```
    """
    ...

def unpack_from(fmt: Union[str, bytes], buffer: ReadableBuffer, offset: int = 0) -> Tuple[Any, ...]:
    """
    Unpack bytes from offset into tuple of values.
    
    Example:
    ```py
    buf = b'padding*\x00\x00\x00\xc3\xf5H@'
    values = struct.unpack_from('I f', buf, 7)
    # (42, 3.140000104904175)
    ```
    """
    ...