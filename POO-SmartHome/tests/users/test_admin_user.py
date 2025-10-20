import pytest
from users.admin_user import AdminUser
from users.standard_user import StandardUser

@pytest.fixture
def admin_user():
    return AdminUser("Lucía", "Martínez", "lucia@example.com", "pass123")

@pytest.fixture
def standard_user():
    return StandardUser("Pedro", "López", "pedro@example.com", "pass456")

def test_inheritance(admin_user):
    assert admin_user.get_is_admin() is True

def test_manage_system(admin_user):
    result = admin_user.manage_system()
    assert "Lucía" in result
    assert "managing the system" in result

def test_change_user_role(admin_user, standard_user):
    assert standard_user.get_is_admin() is False
    result = admin_user.change_user_role(standard_user, True)
    assert "Pedro" in result
    assert standard_user.get_is_admin() is True
