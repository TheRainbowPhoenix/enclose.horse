# gc module: control the garbage collector (MicroPython extension)
from typing import Optional

def enable() -> None:
    """Enable automatic garbage collection."""
    ...

def disable() -> None:
    """Disable automatic garbage collection. Manual collection still possible with gc.collect()."""
    ...

def collect() -> int:
    """Run a garbage collection."""
    ...

def mem_alloc() -> int:
    """Return the number of bytes of heap RAM allocated by Python code (MicroPython only)."""
    ...

def mem_free() -> int:
    """Return the number of bytes of heap RAM available to allocate (MicroPython only)."""
    ...

def threshold(amount: Optional[int] = None) -> int:
    """
    Set or query the GC allocation threshold (MicroPython only).
    If 'amount' is provided, sets the threshold. Returns current threshold.
    """
    ...
