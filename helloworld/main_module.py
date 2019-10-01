"""Main module."""
from .helpers import get_planet


def hello(greeted_person: str) -> str:
    """Greet greeted_person."""
    return f"Hello, {greeted_person}!"


if __name__ == "__main__":
    print(hello(get_planet()))
