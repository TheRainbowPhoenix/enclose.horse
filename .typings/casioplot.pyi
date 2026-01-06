from typing import Literal, Tuple

def show_screen() -> None:
    """Update display with current VRAM contents."""
    ...

def clear_screen() -> None:
    """Fill VRAM with white (clear drawing buffer)."""
    ...

def set_pixel(x: int, y: int, color: Tuple[int, int, int] = (0, 0, 0)) -> None:
    """
    Set pixel color at (x,y) position.
    
    - `color`: RGB tuple (0-255 values)  
    *For performance, pre-store colors instead of recreating tuples.*
    
    Example:
    ```py
    set_pixel(10, 10, (255, 0, 0))  # Red pixel
    ```
    """
    ...

def get_pixel(x: int, y: int) -> Tuple[int, int, int]:
    """
    Get pixel color at (x,y) as RGB tuple.
    
    *Warning: Slow in loops due to tuple allocation.*
    
    Example:
    ```py
    color = get_pixel(10, 10)
    ```
    """
    ...

def draw_string(
    x: int,
    y: int,
    text: str,
    color: Tuple[int, int, int] = (0, 0, 0),
    size: Literal["small", "medium", "large"] = "medium"
) -> None:
    """
    Draw text with top-left corner at (x,y).
    
    - `size`: "small" | "medium" | "large"  
    - Newlines in text become spaces
    
    Example:
    ```py
    draw_string(0, 0, "Hello", (0,0,255), "large")  # Blue large text
    ```
    """
    ...