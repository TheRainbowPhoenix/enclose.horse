from typing import Any, BinaryIO, Optional, TextIO, Union, overload

@overload
def open(name: str, mode: str = 'r', **kwargs: Any) -> TextIO: ...
@overload
def open(name: str, mode: str = 'rb', **kwargs: Any) -> BinaryIO: ...
def open(name: str, mode: str = 'r', **kwargs: Any) -> Union[TextIO, BinaryIO]:
    """
    Open a file with specified mode.
    
    - `mode`: 'r' (text), 'rb' (binary), 'w', 'a', etc.
    - Returns file-like object (TextIO/BinaryIO)
    
    Example:
    ```
    with io.open('data.txt', 'r') as f:
        print(f.read())
    ```
    """
    ...

class StringIO:
    """
    In-memory text stream (like a text-mode file).
    
    Example:
    ```py
    buf = io.StringIO("initial text")
    buf.write("hello")
    print(buf.getvalue())  # "initial texthello"
    ```
    """
    
    def __init__(self, initial_value: str = "", alloc_size: Optional[int] = None) -> None:
        """
        Text I/O implementation using an in-memory buffer.

        The initial_value argument sets the value of object. The newline argument is like the one of TextIOWrapper's constructor.
        """
        ...
    
    def read(self, size: Optional[int] = -1) -> str:
        """
        Read at most size characters, returned as a string.

        If the argument is negative or omitted, read until EOF is reached. Return an empty string at EOF.
        """
        ...

    def write(self, s: str) -> int:
        """
        Write string to file.

        Returns the number of characters written, which is always equal to the length of the string.
        """
        ...
    def seek(self, offset: int, whence: int = 0) -> int: 
        """
        Change stream position.

        Seek to byte offset pos relative to position indicated by whence:

        - `0` : Start of stream (the default). pos should be >= 0;
        - `1` : Current position - pos may be negative;
        - `2` : End of stream - pos usually negative.

        Returns the new absolute position.
        """
        ...
    def tell(self) -> int:
        """Tell the current file position."""
        ...
    def flush(self) -> None:...
    def close(self) -> None:
        """Close the IO object.

        Attempting any further operation after the object is closed will raise a ValueError.

        This method has no effect if the file is already closed.
        """
        ...
    def getvalue(self) -> str:
        """Retrieve the entire contents of the object."""
        ...

class BytesIO:
    """
    In-memory binary stream (like a binary-mode file).
    
    Example:
    ```py
    buf = io.BytesIO(b"initial")
    buf.write(b"\x01\x02")
    print(buf.getvalue())  # b'initial\x01\x02'
    ```
    """
    
    def __init__(self, initial_value: bytes = b"", alloc_size: Optional[int] = None) -> None:
        """Buffered I/O implementation using an in-memory bytes buffer."""
        ...
    
    def read(self, size: Optional[int] = -1) -> bytes:
        """
        Read at most size bytes, returned as a bytes object.

        If the size argument is negative, read until EOF is reached. Return an empty bytes object at EOF.
        """
        ...
    
    def write(self, s: bytes) -> int:
        """Write bytes to file.

        Return the number of bytes written."""
        ...
    
    def seek(self, offset: int, whence: int = 0) -> int:
        """
        Change stream position.

        Seek to byte offset pos relative to position indicated by whence:

        - `0` : Start of stream (the default). pos should be >= 0;
        - `1` : Current position - pos may be negative;
        - `2` : End of stream - pos usually negative.

        Returns the new absolute position.
        """
        ...
    def tell(self) -> int:
        """Current file position, an integer."""
        ...
    def flush(self) -> None:
        """Does nothing."""
        ...
    def close(self) -> None:
        """Disable all I/O operations."""
        ...
    def getvalue(self) -> bytes:
        """Retrieve the entire contents of the BytesIO object."""
        ...