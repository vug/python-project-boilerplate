from typing import Any

from .helpers import get_planet


# TODO: update
class HTTP(object):
    def __init__(self, request: str):
        self.request = request

    def parse_request(self) -> None:
        pass

    def respond(self, obj: Any) -> None:
        pass


class Request(object):
    def __init__(self, request: str):
        self.request = request


def hello(greeted_person: str) -> str:
    return f"Hello, {greeted_person}!"


if __name__ == "__main__":
    print(hello(get_planet()))
