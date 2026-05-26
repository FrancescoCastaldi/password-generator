import pytest
from src.generator import generate_password, ALGORITHMS


@pytest.mark.parametrize("algo", ALGORITHMS)
def test_length(algo):
    pwd = generate_password(algorithm=algo, length=32)
    assert len(pwd) == 32


@pytest.mark.parametrize("algo", ALGORITHMS)
def test_uniqueness(algo):
    passwords = {generate_password(algorithm=algo, length=32) for _ in range(100)}
    assert len(passwords) == 100


def test_invalid_algorithm():
    with pytest.raises(ValueError):
        generate_password(algorithm="fake_algo")
