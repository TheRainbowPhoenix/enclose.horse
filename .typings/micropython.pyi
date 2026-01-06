# micropython module: access and control MicroPython internals

from typing import Any, Callable, Optional

def const(expr: Any) -> Any:
    """
    Declare a constant value to enable compiler optimizations.
    
    Usage:
        from micropython import const
        CONST_X = const(123)
    """
    ...

def opt_level(level: Optional[int] = None) -> Optional[int]:
    """
    Set or get the current compiler optimization level.
    - If `level` is provided, sets the level and returns None.
    - If omitted, returns the current optimization level.
    """
    ...

# def alloc_emergency_exception_buf(size: int) -> None:
#     """
#     Allocate emergency exception buffer for use in memory-critical contexts like interrupts.
#     A recommended size is around 100 bytes.
#     """
#     ...

# def mem_info(verbose: Optional[int] = None) -> None:
#     """
#     Print memory usage info. Prints more details if `verbose` is provided.
#     """
#     ...

# def qstr_info(verbose: Optional[int] = None) -> None:
#     """
#     Print information about interned strings. More details if `verbose` is provided.
#     """
#     ...

# def stack_use() -> int:
#     """
#     Return the current stack usage (in bytes). Best used for tracking differences over time.
#     """
#     ...

def heap_lock() -> int:
    """
    Lock the heap (disable memory allocation). Returns the new lock depth.
    """
    ...

def heap_unlock() -> int:
    """
    Unlock the heap. Returns the current lock depth after unlocking.
    """
    ...

# def heap_locked() -> int:
#     """
#     Return the current heap lock depth.
#     Note: May not be available on all ports.
#     """
#     ...

def kbd_intr(chr: int) -> None:
    """
    Set the interrupt character (e.g. Ctrl-C = 3). Use -1 to disable Ctrl-C capture.
    """
    ...

# def schedule(func: Callable[[Any], None], arg: Any) -> None:
#     """
#     Schedule `func(arg)` to run soon in the main context (e.g., from an IRQ).
#     Raises RuntimeError if the schedule queue is full.
#     """
#     ...
