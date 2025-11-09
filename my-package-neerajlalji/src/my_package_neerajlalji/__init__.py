def hello() -> str:
    """Return a greeting message from the package.

    Returns:
        str: A greeting message with the package version.

    Example:
        >>> hello()
        'Hello from my-package-neerajlalji! v0.1.2'
    """
    return "🎉 Hello from my-package-neerajlalji!"


def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        float: The sum of a and b.

    Example:
        >>> add_numbers(5, 3)
        8.0
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    return a + b


def reverse_string(text: str) -> str:
    """Reverse a given string.

    Args:
        text: The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: A list of numbers to average.

    Returns:
        float: The average of the numbers.

    Raises:
        ValueError: If the list is empty.
        TypeError: If any element is not a number.

    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([10.5, 20.5])
        15.5
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a string.

    Args:
        text: The string to capitalize.

    Returns:
        str: The string with each word capitalized.

    Example:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python is awesome")
        'Python Is Awesome'
    """
    return text.title()
