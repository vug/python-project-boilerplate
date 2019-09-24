from helpers import get_planet


def hello(greeted_person: str) -> str:
    print(f"Hello, {greeted_person}!")


if __name__ == "__main__":
    hello(get_planet())
