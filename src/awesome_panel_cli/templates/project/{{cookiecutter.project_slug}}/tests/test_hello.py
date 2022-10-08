"""A Basic test file"""
from {{cookiecutter.package_slug}} import VERSION


def test_hello():
    """A basic test function"""
    # Given nothing
    # When
    print(f"hello {VERSION}")
    # Then no errors
