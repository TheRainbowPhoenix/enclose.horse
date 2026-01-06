from typing import Any, List, Optional, Sequence, Tuple, Union

def choice(seq: Sequence[Any]) -> Any:
    """
    Choose random element from sequence.
    
    Example:
    ```
    color = random.choice(['red', 'green', 'blue'])
    ```
    """
    ...

def getrandbits(n: int) -> int:
    """
    Generate integer with n random bits (0-32).
    
    Example:
    ```
    num = random.getrandbits(8)  # 8-bit random number (0-255)
    ```
    """
    ...

def randint(a: int, b: int) -> int:
    """
    Random integer N where a <= N <= b.
    
    Example:
    ```
    dice = random.randint(1, 6)  # Standard die roll
    ```
    """
    ...

def random() -> float:
    """
    Random float 0.0 <= N < 1.0.
    
    Example:
    ```
    if random.random() < 0.5:  # 50% probability
        print("Heads")
    ```
    """
    ...

def randrange(start: int, stop: Optional[int] = None, step: int = 1) -> int:
    """
    Random integer from range(start, stop[, step]).
    
    Examples:
    ```
    random.randrange(10)     # 0-9
    random.randrange(1, 10) # 1-9
    random.randrange(1, 10, 2)  # Odd numbers 1-9
    ```
    """
    ...

def seed(n: Optional[int] = None) -> None:
    """
    Initialize random number generator.
    
    - `n`: Seed value (None uses hardware random if available)
    
    Example:
    ```
    random.seed(42)  # Fixed seed for reproducible results
    ```
    """
    ...

def uniform(a: float, b: float) -> float:
    """
    Random float N where a <= N <= b (or b <= N <= a if b < a).
    
    Example:
    ```
    temp = random.uniform(-10.5, 30.0)  # Temperature range
    ```
    """
    ...
