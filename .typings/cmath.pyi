from typing import Tuple, Union, Final

# Complex number type hint
Complex = Union[complex, Tuple[float, float]]

# Constants
e: Final[float] = ...
"""
base of the natural logarithm
"""

pi: Final[float] = ...
"""
the ratio of a circle's circumference to its diameter
"""

def cos(z: Complex) -> complex:
    """
    Cosine of complex number z.
    
    Example:
    ```
    cmath.cos(1 + 1j)  # ≈ 0.8337 - 0.9889j
    ```
    """
    ...

def exp(z: Complex) -> complex:
    """
    Exponential of z (e^z).
    
    Example:
    ```
    cmath.exp(1j * cmath.pi)  # ≈ -1+0j (Euler's identity)
    ```
    """
    ...

def log(z: Complex) -> complex:
    """
    Natural logarithm (base e) of z.
    
    Branch cut along negative real axis.
    
    Example:
    ```
    cmath.log(1j)  # ≈ 0 + 1.5708j
    ```
    """
    ...

# def log10(z: Complex) -> complex:
#     """
#     Base-10 logarithm of z.
    
#     Branch cut along negative real axis.
    
#     Example:
#     ```
#     cmath.log10(100 + 100j)  # ≈ 2.1505 + 0.3218j
#     ```
#     """
#     ...

def phase(z: Complex) -> float:
    """
    Phase angle (in radians) of z in range (-π, π].
    
    Example:
    ```
    cmath.phase(1 + 1j)  # ≈ 0.7854 (π/4)
    ```
    """
    ...

def polar(z: Complex) -> Tuple[float, float]:
    """
    Convert z to polar form (magnitude, phase).
    
    Example:
    ```
    r, phi = cmath.polar(1 + 1j)  # ≈ (1.4142, 0.7854)
    ```
    """
    ...

def rect(r: float, phi: float) -> complex:
    """
    Convert polar coordinates to complex number.
    
    - `r`: Magnitude
    - `phi`: Phase angle (radians)
    
    Example:
    ```
    cmath.rect(1.4142, cmath.pi/4)  # ≈ 1+1j
    ```
    """
    ...

def sin(z: Complex) -> complex:
    """
    Sine of complex number z.
    
    Example:
    ```
    cmath.sin(1 + 1j)  # ≈ 1.2985 + 0.6350j
    ```
    """
    ...

def sqrt(z: Complex) -> complex:
    """
    Principal square root of z.
    
    Example:
    ```
    cmath.sqrt(-1)  # 1j
    ```
    """
    ...