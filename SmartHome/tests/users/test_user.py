import pytest
from users.user import User

@pytest.fixture
def sample_user():
    return User("Carlos", "Gómez", "carlos@example.com", "1234", True)

def test_getters(sample_user):
    assert sample_user.get_name() == "Carlos"
    assert sample_user.get_lastname() == "Gómez"
    assert sample_user.get_mail() == "carlos@example.com"
    assert sample_user.get_password() == "1234"
    assert sample_user.get_is_admin() is True

def test_setters(sample_user):
    sample_user.set_name("Juan")
    sample_user.set_lastname("Pérez")
    sample_user.set_mail("juan@example.com")
    sample_user.set_password("newpass")
    sample_user.set_is_admin(False)

    assert sample_user.get_name() == "Juan"
    assert sample_user.get_lastname() == "Pérez"
    assert sample_user.get_mail() == "juan@example.com"
    assert sample_user.get_password() == "newpass"
    assert sample_user.get_is_admin() is False

def test_register(sample_user):
    assert "Carlos" in sample_user.register()

def test_login(sample_user):
    assert sample_user.login("carlos@example.com", "1234")
    assert not sample_user.login("carlos@example.com", "wrong")
