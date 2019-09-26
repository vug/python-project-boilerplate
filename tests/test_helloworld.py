from helloworld import helloworld


def test_hello():
    assert helloworld.hello("World") == "Hello, World!"
