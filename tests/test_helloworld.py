from helloworld import main_module


def test_hello():
    assert main_module.hello("World") == "Hello, World!"
