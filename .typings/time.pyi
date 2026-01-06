from typing import Optional, Tuple, Union

def monotonic() -> float:
    """
    Returns the clock value at the time the function is called.
    Monotonic clock, cannot go backward.

    Example:
        tour = monotonic()
        # ...
        if monotonic() - tour > 6.5:
            # ...
    """
    ...

# def gmtime(secs: Optional[int] = None) -> Tuple[int, int, int, int, int, int, int, int]:
#     """
#     Convert seconds since Epoch to UTC time tuple.
    
#     Args:
#         secs: Seconds since Epoch. Uses current time if None.
#     Returns:
#         (year, month, day, hour, minute, second, weekday, yearday)
#     Example:
#         print(gmtime())  # (2023, 8, 4, 15, 30, 0, 3, 216)
#     """
#     ...

# def localtime(secs: Optional[int] = None) -> Tuple[int, int, int, int, int, int, int, int]:
#     """
#     Convert seconds since Epoch to local time tuple.
    
#     Args:
#         secs: Seconds since Epoch. Uses current time if None.
#     Returns:
#         Same format as gmtime(), but in local timezone
#     """
#     ...

# def mktime(time_tuple: Tuple[int, int, int, int, int, int, int, int]) -> int:
#     """
#     Convert local time tuple to seconds since 2000-01-01.
    
#     Inverse of localtime().
#     Example:
#         mktime((2023, 8, 4, 12, 0, 0, 4, 216))  # returns 742521600
#     """
#     ...

def sleep(seconds: Union[int, float]) -> None:
    """
    Delay execution for given seconds.
    
    Note:
        Float support varies by hardware. Prefer sleep_ms/sleep_us
        for precise timing.
    Example:
        sleep(1.5)  # sleep 1.5 seconds
    """
    ...

def sleep_ms(ms: int) -> None:
    """
    Precise millisecond sleep.
    
    Args:
        ms: Milliseconds to wait (>= 0)
    Example:
        sleep_ms(500)  # half-second delay
    """
    ...

def sleep_us(us: int) -> None:
    """
    Microsecond-resolution sleep.
    
    Args:
        us: Microseconds to wait (>= 0)
    Example:
        sleep_us(100)  # delay 100μs
    """
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """
    Add offset to ticks value (wrapping-safe).
    
    Args:
        ticks: Value from ticks_ms/us/cpu()
        delta: Number to add (can be negative)
    Example:
        deadline = ticks_add(ticks_ms(), 200)  # 200ms from now
    """
    ...

def ticks_cpu() -> int:
    """
    Highest resolution system timer.
    
    Note:
        Not available on all ports. Useful for microbenchmarks.
    """
    ...

def ticks_diff(ticks1: int, ticks2: int) -> int:
    """
    Calculate signed difference between ticks.
    
    Returns:
        ticks1 - ticks2 (accounting for wrapping)
    Example:
        if ticks_diff(deadline, ticks_ms()) > 0:  # time left
    """
    ...


def ticks_ms() -> int:
    """
    Get monotonic millisecond counter.
    
    Wraps around periodically. Use ticks_diff() for timing.
    Value is arbitrary reference point.
    Example:
        start = ticks_ms()
        sleep_ms(50)
        print(ticks_diff(ticks_ms(), start))  # ~50
    """
    ...

def ticks_us() -> int:
    """
    Microsecond-resolution monotonic counter.
    
    Same wrapping behavior as ticks_ms().
    """
    ...


def time() -> int:
    """
    Get seconds since Epoch.
    
    Note:
        Epoch varies by port (1970 or 2000). Accuracy depends
        on RTC being properly set.
    """
    ...

def time_ns() -> int:
    """
    Nanosecond-resolution time since Epoch.
    
    Returns:
        May be large integer (heap allocation)
    Example:
        print(time_ns())  # 1691166600123456789
    """
    ...