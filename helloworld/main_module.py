from .helpers import get_planet


def hello(greeted_person: str) -> str:
    return f"Hello, {greeted_person}!"


if __name__ == "__main__":
    print(hello(get_planet()))
